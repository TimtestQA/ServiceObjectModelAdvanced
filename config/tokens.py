import os
from dotenv import load_dotenv

load_dotenv()


TOKENS = {
    "default": os.getenv("DEFAULT_TOKEN"),
    "admin": os.getenv("ADMIN_TOKEN"),
    "moderator": os.getenv("MODERATOR_TOKEN"),
    "guest": os.getenv("GUEST_TOKEN"),
}