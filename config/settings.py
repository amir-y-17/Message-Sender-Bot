import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_TOKEN = os.getenv("EITAA_API_TOKEN")

CHANNEL_IDS = [-1002853108145]
EITAA_CHANNEL = 10779535


def get_eitaa_api_url(method_name: str) -> str:
    return f"https://eitaayar.ir/api/{API_TOKEN}/{method_name}"
