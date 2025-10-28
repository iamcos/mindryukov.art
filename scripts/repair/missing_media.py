import asyncio
import os
from telethon import TelegramClient

from scripts.downloader.config import API_ID, API_HASH, SESSION_NAME, CHANNEL, POSTS_JSON, MEDIA_DIR
from scripts.downloader.utils import load_json


async def main() -> None:
    posts = load_json(POSTS_JSON) or []
    os.makedirs(MEDIA_DIR, exist_ok=True)

    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        for p in posts:
            if p.get("media") and not p.get("media_path"):
                msg_id = p["id"]
                msg = await client.get_messages(CHANNEL, ids=msg_id)
                if msg:
                    path = await client.download_media(msg, file=MEDIA_DIR)
                    if path:
                        p["media_path"] = os.path.relpath(path)
    # Write back the updated posts
    if posts:
        from scripts.downloader.utils import save_json
        save_json(POSTS_JSON, posts)


if __name__ == "__main__":
    asyncio.run(main())
