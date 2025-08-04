from config.settings import TOKEN
from bot.telegram_client import TelegramClient
from telegram.ext import MessageHandler, filters
from bot.handlers.channel_post_handlers import get_new_message


def main():
    client = TelegramClient(token=TOKEN)

    handlers = [MessageHandler(filters=filters.ALL, callback=get_new_message)]

    client.add_handlers(handlers)

    client.start()


if __name__ == "__main__":
    main()
