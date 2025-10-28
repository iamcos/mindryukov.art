import asyncio
import os
from telethon import TelegramClient
from telethon.tl.types import Message

from .config import API_ID, API_HASH, CHANNEL, SESSION_NAME, POSTS_JSON, MEDIA_DIR
from .utils import append_post, download_media, serialize_message


async def process_message(client: TelegramClient, message: Message) -> None:
    record = serialize_message(message)
    if message.media:
        media_path = await download_media(client, message, MEDIA_DIR)
        if media_path:
            record["media_path"] = os.path.relpath(media_path)
    append_post(POSTS_JSON, record)


async def run() -> None:
    if not API_ID or not API_HASH:
        raise RuntimeError("API_ID/API_HASH not configured. Set environment or .env.")

    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        async for message in client.iter_messages(CHANNEL, reverse=True):
            await process_message(client, message)


if __name__ == "__main__":
    asyncio.run(run())
