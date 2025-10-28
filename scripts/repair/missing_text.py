import asyncio
from telethon import TelegramClient

from scripts.downloader.config import API_ID, API_HASH, SESSION_NAME, CHANNEL, POSTS_JSON
from scripts.downloader.utils import load_json, save_json


async def main() -> None:
    posts = load_json(POSTS_JSON) or []
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        for p in posts:
            if p.get("message") is None:
                msg_id = p["id"]
                msg = await client.get_messages(CHANNEL, ids=msg_id)
                if msg:
                    p["message"] = msg.message
    save_json(POSTS_JSON, posts)


if __name__ == "__main__":
    asyncio.run(main())
