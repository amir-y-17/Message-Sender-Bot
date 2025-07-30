import requests
from telegram import Update
from utils import formatters
from telegram.ext import ContextTypes
from config.settings import *


async def get_new_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    if message.chat_id in CHANNEL_IDS:
        message_formatter = formatters.get_formatter(message)
        data = message_formatter.format()
