import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_TOKEN = os.getenv("EITAA_API_TOKEN")

TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
EITAA_CHANNEL_ID = os.getenv("EITAA_CHANNEL_ID")


def get_eitaa_api_url(method_name: str) -> str:
    return f"https://eitaayar.ir/api/{API_TOKEN}/{method_name}"
