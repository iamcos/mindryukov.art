#!/usr/bin/env python3
"""
Script to extract messages from "Hostel Roi" Telegram chat,
extract links, follow them for descriptions, and create a tracking JSON file.
"""

import asyncio
import json
import re
import os
from datetime import datetime
from urllib.parse import urlparse, urljoin
import sys

try:
    from telethon import TelegramClient
    from telethon.tl.types import MessageEntityUrl, MessageEntityTextUrl
except ImportError:
    print("Telethon not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"])
    from telethon import TelegramClient
    from telethon.tl.types import MessageEntityUrl, MessageEntityTextUrl

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("requests/BeautifulSoup not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"])
    import requests
    from bs4 import BeautifulSoup


def extract_urls(text, entities=None):
    """Extract URLs from message text and entities."""
    urls = set()
    
    # Extract URLs from text using regex
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    found_urls = re.findall(url_pattern, text)
    urls.update(found_urls)
    
    # Extract URLs from entities if available
    if entities:
        for entity in entities:
            if isinstance(entity, (MessageEntityUrl, MessageEntityTextUrl)):
                if hasattr(entity, 'url'):
                    urls.add(entity.url)
                elif isinstance(entity, MessageEntityUrl):
                    # Extract URL from text using entity offset and length
                    start = entity.offset
                    end = start + entity.length
                    url_text = text[start:end]
                    if url_text.startswith('http'):
                        urls.add(url_text)
    
    # Also check for t.me links and other common patterns
    telegram_pattern = r't\.me/[a-zA-Z0-9_]+'
    telegram_links = re.findall(telegram_pattern, text)
    for link in telegram_links:
        urls.add(f'https://{link}')
    
    return list(urls)


def get_link_description(url, timeout=5):
    """Follow a link and extract description/title."""
    try:
        # Handle Telegram links specially
        if 't.me' in url or 'telegram.org' in url:
            return "Telegram link - may contain contact information"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try to get meta description
            meta_desc = soup.find('meta', property='og:description')
            if meta_desc:
                desc = meta_desc.get('content', '').strip()
                if desc:
                    return desc
            
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                desc = meta_desc.get('content', '').strip()
                if desc:
                    return desc
            
            # Try to get title
            title = soup.find('title')
            if title:
                title_text = title.get_text().strip()
                if title_text:
                    return title_text
            
            # Try to get first paragraph
            p = soup.find('p')
            if p:
                p_text = p.get_text().strip()[:200]
                if p_text:
                    return p_text
                
    except requests.exceptions.Timeout:
        return "Timeout: Link took too long to respond"
    except requests.exceptions.RequestException as e:
        return f"Error fetching: {str(e)[:100]}"
    except Exception as e:
        return f"Error: {str(e)[:100]}"
    
    return None


async def find_chat(client, chat_name):
    """Find a chat by name."""
    async for dialog in client.iter_dialogs():
        if chat_name.lower() in dialog.name.lower():
            return dialog.entity
    return None


async def extract_messages(client, chat_entity):
    """Extract all messages from the chat."""
    messages_data = []
    seen_contacts = {}  # Track unique contacts/links
    
    print(f"Extracting messages from {chat_entity}...")
    
    async for message in client.iter_messages(chat_entity, reverse=False):
        if not message.text:
            continue
            
        urls = extract_urls(message.text, message.entities)
        
        # Check for contact information patterns
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_pattern = r'\+?[\d\s\-\(\)]{10,}'
        telegram_user_pattern = r'@[a-zA-Z0-9_]{5,}'
        
        has_email = bool(re.search(email_pattern, message.text))
        has_phone = bool(re.search(phone_pattern, message.text))
        has_telegram_user = bool(re.search(telegram_user_pattern, message.text))
        has_link = bool(urls)
        has_contact_keywords = any(keyword in message.text.lower() for keyword in [
            'contact', 'reach', 'email', 'phone', 'call', 'whatsapp', 'telegram',
            'message', 'dm', 'pm', 'connect', 'get in touch'
        ])
        
        # Include message if it has any contact information
        if has_link or has_email or has_phone or has_telegram_user or has_contact_keywords:
            # Extract contact information
            contact_info = {
                'message_id': message.id,
                'date': message.date.isoformat() if message.date else None,
                'sender': None,
                'text': message.text,
                'links': [],
                'descriptions': {},
                'status': 'not_contacted',  # not_contacted, contacted, replied, meeting_scheduled, etc.
                'notes': '',
                'last_contact_date': None,
                'contact_method': None,  # email, telegram, phone, website, etc.
                'priority': 'medium',  # low, medium, high
                'tags': [],
                'next_action': None,  # What to do next
                'follow_up_date': None
            }
            
            # Get sender info if available
            if message.sender:
                try:
                    sender = await message.get_sender()
                    if sender:
                        contact_info['sender'] = {
                            'id': sender.id if hasattr(sender, 'id') else None,
                            'username': getattr(sender, 'username', None),
                            'first_name': getattr(sender, 'first_name', None),
                            'last_name': getattr(sender, 'last_name', None),
                        }
                except:
                    pass
            
            # Process each URL
            for url in urls:
                contact_info['links'].append(url)
                
                # Get description from link
                print(f"  Fetching description for {url}...")
                description = get_link_description(url)
                if description:
                    contact_info['descriptions'][url] = description
                
            # Extract contact information from text (do this once, not per URL)
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, message.text)
            if emails:
                contact_info['contact_method'] = 'email'
                contact_info['notes'] += f"Email: {', '.join(emails)}\n"
            
            phone_pattern = r'\+?[\d\s\-\(\)]{10,}'
            phones = re.findall(phone_pattern, message.text)
            # Filter out false positives (like years, message IDs, etc.)
            phones = [p for p in phones if len(re.sub(r'[\s\-\(\)]', '', p)) >= 10]
            if phones:
                if not contact_info['contact_method']:
                    contact_info['contact_method'] = 'phone'
                contact_info['notes'] += f"Phone: {', '.join(phones)}\n"
            
            # Check for Telegram username mentions
            telegram_user_pattern = r'@[a-zA-Z0-9_]{5,}'
            telegram_users = re.findall(telegram_user_pattern, message.text)
            if telegram_users:
                if not contact_info['contact_method']:
                    contact_info['contact_method'] = 'telegram'
                contact_info['notes'] += f"Telegram: {', '.join(telegram_users)}\n"
            
            # Extract additional context from message
            if message.reply_to:
                contact_info['notes'] += f"Reply to message ID: {message.reply_to.reply_to_msg_id}\n"
            
            messages_data.append(contact_info)
            
            # Small delay to avoid rate limiting
            await asyncio.sleep(0.1)
    
    return messages_data


async def main():
    """Main function."""
    # Get API credentials from environment or ask user
    api_id = os.environ.get('TELEGRAM_API_ID')
    api_hash = os.environ.get('TELEGRAM_API_HASH')
    
    if not api_id or not api_hash:
        print("Please set TELEGRAM_API_ID and TELEGRAM_API_HASH environment variables")
        print("Or enter them now:")
        api_id = input("API ID: ").strip()
        api_hash = input("API Hash: ").strip()
    
    if not api_id or not api_hash:
        print("API credentials are required!")
        return
    
    # Try to find session file
    session_files = [
        'session_name.session',
        '../session_name.session',
        'scripts/legacy/telegram-mcp/session_name.session'
    ]
    
    session_path = None
    for path in session_files:
        if os.path.exists(path):
            session_path = path
            break
    
    if not session_path:
        # Use default session name
        session_path = 'session_name'
    
    print(f"Using session: {session_path}")
    print(f"API ID: {api_id[:4]}...")
    
    # Create output directory
    output_dir = 'hostel_roi_tracking'
    os.makedirs(output_dir, exist_ok=True)
    
    # Connect to Telegram
    client = TelegramClient(session_path, int(api_id), api_hash)
    
    try:
        await client.start()
        print("Connected to Telegram!")
        
        # Find the chat
        print("\nLooking for 'Hostel Roi' chat...")
        chat_entity = await find_chat(client, "Hostel Roi")
        
        if not chat_entity:
            print("Chat 'Hostel Roi' not found!")
            print("\nAvailable chats:")
            async for dialog in client.iter_dialogs(limit=20):
                print(f"  - {dialog.name}")
            return
        
        print(f"Found chat: {chat_entity}")
        
        # Extract messages
        print("\nExtracting messages...")
        messages_data = await extract_messages(client, chat_entity)
        
        print(f"\nExtracted {len(messages_data)} messages with links/contacts")
        
        # Create output structure
        output_data = {
            'chat_name': 'Hostel Roi',
            'extracted_at': datetime.now().isoformat(),
            'total_contacts': len(messages_data),
            'contacts': messages_data
        }
        
        # Save to JSON
        output_file = os.path.join(output_dir, 'hostel_roi_contacts.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Saved {len(messages_data)} contacts to {output_file}")
        
    finally:
        await client.disconnect()


if __name__ == '__main__':
    asyncio.run(main())

