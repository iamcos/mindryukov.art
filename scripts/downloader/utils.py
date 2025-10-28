import json
import os
from typing import Any, Dict

from telethon.tl.types import Message


def load_json(path: str) -> Any:
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


essential_post_fields = [
    "id",
    "date",
    "message",
    "media",
    "reply_to",
    "views",
    "forwards",
]


def append_post(posts_path: str, record: Dict[str, Any]) -> None:
    posts = load_json(posts_path) or []
    # Keep minimal size by storing only essential fields + extras
    minimal = {k: record.get(k) for k in essential_post_fields}
    for k, v in record.items():
        if k not in minimal:
            minimal[k] = v
    posts.append(minimal)
    save_json(posts_path, posts)


async def download_media(client, message: Message, media_dir: str) -> str:
    file_path = await client.download_media(message, file=media_dir)
    return file_path or ""


def serialize_message(message: Message) -> Dict[str, Any]:
    return {
        "id": message.id,
        "date": message.date.isoformat() if message.date else None,
        "message": message.message,
        "media": bool(message.media),
        "reply_to": getattr(getattr(message, "reply_to", None), "reply_to_msg_id", None),
        "views": getattr(message, "views", None),
        "forwards": getattr(message, "forwards", None),
    }
