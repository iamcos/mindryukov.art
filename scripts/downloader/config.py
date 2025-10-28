from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
CHANNEL = os.getenv("CHANNEL", "@mindryukov_films")
SESSION_NAME = os.getenv("SESSION_NAME", "session_name")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
MEDIA_DIR = os.path.join(BASE_DIR, "media")
POSTS_JSON = os.path.join(DATA_DIR, "posts_metadata", "posts.json")
PROFILE_JSON = os.path.join(DATA_DIR, "profile_info", "profile.json")
WEBSITE_SUMMARY_JSON = os.path.join(DATA_DIR, "website_summary.json")

os.makedirs(os.path.join(DATA_DIR, "posts_metadata"), exist_ok=True)
os.makedirs(os.path.join(DATA_DIR, "profile_info"), exist_ok=True)
os.makedirs(os.path.join(MEDIA_DIR, "photos"), exist_ok=True)
os.makedirs(os.path.join(MEDIA_DIR, "videos"), exist_ok=True)
os.makedirs(os.path.join(MEDIA_DIR, "audio"), exist_ok=True)
os.makedirs(os.path.join(MEDIA_DIR, "documents"), exist_ok=True)
