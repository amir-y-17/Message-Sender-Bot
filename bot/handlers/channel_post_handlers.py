import requests
from telegram import Update
from utils import formatters, downloaders
from telegram.ext import ContextTypes
from config.settings import *
from core.forward import get_forwarder


async def get_new_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    if message.chat_id == int(TELEGRAM_CHANNEL_ID):
        message_formatter = formatters.get_formatter(message)
        formatted_data = message_formatter.format()

        message_type = formatted_data["type"]
        method_name = "sendMessage" if message_type == "text" else "sendFile"

        url = get_eitaa_api_url(method_name)
        forwarder = get_forwarder(message_type=formatted_data["type"], api_url=url)

        status, result = forwarder.forward(formatted_data)

        if status == 200:
            print(
                f"[INFO] Message sent successfully from channel {message.chat_id} with status {status}"
            )
        else:
            print(
                f"[ERROR] Failed to send message from channel {message.chat_id}. Status: {status}, Response: {result}"
            )
