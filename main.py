from telegram import Update
from config.settings import TOKEN
from bot.telegram_client import TelegramClient
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters
from bot.handlers.channel_post_handlers import get_new_message


# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(update.effective_chat.id, text="Hello")


def main():
    client = TelegramClient(token=TOKEN)

    handlers = [MessageHandler(filters=filters.ALL, callback=get_new_message)]

    client.add_handlers(handlers)

    client.start()


if __name__ == "__main__":
    main()
