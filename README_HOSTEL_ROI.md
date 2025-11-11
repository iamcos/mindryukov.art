# Hostel Roi Contact Tracking

This script extracts messages from the "Hostel Roi" Telegram chat, identifies links and contact information, and creates a tracking JSON file for managing outreach efforts.

## Setup

1. **Install dependencies:**
```bash
pip install telethon requests beautifulsoup4
```

2. **Get Telegram API credentials:**
   - Go to https://my.telegram.org
   - Login with your phone number
   - Go to "API development tools"
   - Create an application to get `api_id` and `api_hash`

3. **Set environment variables (optional):**
```bash
export TELEGRAM_API_ID=your_api_id
export TELEGRAM_API_HASH=your_api_hash
```

Or enter them when prompted by the script.

## Usage

```bash
python extract_hostel_roi.py
```

The script will:
1. Connect to Telegram using your session file
2. Find the "Hostel Roi" chat
3. Extract all messages containing links or contact information
4. Follow links to extract descriptions/metadata
5. Save everything to `hostel_roi_tracking/hostel_roi_contacts.json`

## Output Structure

The JSON file contains:
- `chat_name`: Name of the chat
- `extracted_at`: When the extraction was performed
- `total_contacts`: Number of contacts found
- `contacts`: Array of contact objects, each with:
  - `message_id`: Telegram message ID
  - `date`: When the message was sent
  - `sender`: Information about the message sender
  - `text`: Full message text
  - `links`: Array of URLs found in the message
  - `descriptions`: Object mapping URLs to their descriptions
  - `status`: Current status (not_contacted, contacted, replied, etc.)
  - `notes`: Additional notes
  - `contact_method`: How to contact (email, telegram, phone, etc.)
  - `priority`: Priority level (low, medium, high)
  - `tags`: Tags for categorization
  - `next_action`: What to do next
  - `follow_up_date`: When to follow up

## Status Values

- `not_contacted`: Haven't reached out yet
- `contacted`: Initial message sent
- `replied`: They replied
- `meeting_scheduled`: Meeting/appointment scheduled
- `in_progress`: Ongoing conversation/project
- `completed`: Task completed
- `not_interested`: They declined
- `no_response`: No response after contact

## Tracking Progress

You can edit the JSON file directly to update status, add notes, set priorities, etc. The file is designed to be human-readable and editable.

## Notes

- The script respects rate limits and adds small delays between requests
- Link descriptions are fetched from web pages when possible
- Telegram links are handled specially (they may contain usernames/contact info)
- The script extracts emails, phone numbers, and Telegram usernames from message text



