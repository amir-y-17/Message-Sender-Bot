import requests
from telegram import Update
from utils import formatters, downloaders
from telegram.ext import ContextTypes
from config.settings import *
from core.forward import get_forwarder


async def get_new_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    if message.chat_id in CHANNEL_IDS:
        message_formatter = formatters.get_formatter(message)
        formatted_data = message_formatter.format()

        message_type = formatted_data["type"]
        method_name = "sendMessage" if message_type == "text" else "sendFile"

        url = get_eitaa_api_url(method_name)
        forwarder = get_forwarder(message_type=formatted_data["type"], api_url=url)

        forwarder.forward(formatted_data)
