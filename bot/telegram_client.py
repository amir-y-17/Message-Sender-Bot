from telegram.ext import ApplicationBuilder


class TelegramClient:
    """
    A client wrapper for interacting with the Telegram Bot API using an application builder.
    Attributes:
        token (str): The bot token used for authentication with the Telegram API.
        application: The underlying application instance managing the bot.
    Methods:
        add_handlers(handlers):
            Adds a list of handler objects to the application for processing incoming updates.
        start():
            Starts the bot by running the polling loop to listen for incoming messages and events.
    """

    def __init__(self, token: str):
        self.token = token
        self.application = ApplicationBuilder().token(self.token).build()

    def add_handlers(self, handlers):
        for handler in handlers:
            self.application.add_handler(handler)

    def start(self):
        self.application.run_polling()
