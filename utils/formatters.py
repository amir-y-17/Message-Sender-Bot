from config.settings import *
import requests


# Base class
class BaseMessageFormatter:
    def __init__(self, message):
        self.message = message

    def format(self) -> dict:
        pass


# Formatter subclasses
class TextMessageFormatter(BaseMessageFormatter):
    def format(self) -> dict:
        data = {
            "type": "text",
            "text": self.message.text,
            "chat_id": EITAA_CHANNEL,
            "pin": 0,
        }
        return data


class PhotoMessageFormatter(BaseMessageFormatter):
    def format(self) -> dict:

        data = {
            "type": "file",
            "caption": self.message.caption,
            "file_id": self.message.photo[-1].file_id,
            "chat_id": EITAA_CHANNEL,
        }
        return data


class VideoMessageFormatter(BaseMessageFormatter):
    def format(self) -> dict:
        data = {
            "type": "file",
            "caption": self.message.caption,
            "file_id": self.message.video.file_id,
            "chat_id": EITAA_CHANNEL,
        }
        return data


class AudioMessageFormatter(BaseMessageFormatter):
    def format(self) -> dict:
        data = {
            "type": "file",
            "caption": self.message.caption,
            "file_id": self.message.audio.file_id,
            "chat_id": EITAA_CHANNEL,
        }
        return data


class VoiceMessageFormatter(BaseMessageFormatter):
    def format(self) -> dict:
        data = {
            "type": "file",
            "caption": "",
            "file_id": self.message.voice.file_id,
            "chat_id": EITAA_CHANNEL,
        }
        return data


class DocumentMessageFormatter(BaseMessageFormatter):
    def format(self) -> dict:
        data = {
            "type": "file",
            "caption": self.message.caption,
            "file_id": self.message.document.file_id,
            "chat_id": EITAA_CHANNEL,
        }
        return data


# Factory function
def get_formatter(message):
    if message.text:
        return TextMessageFormatter(message)

    if message.photo:
        return PhotoMessageFormatter(message)

    if message.video:
        return VideoMessageFormatter(message)

    if message.audio:
        return AudioMessageFormatter(message)

    if message.voice:
        return VoiceMessageFormatter(message)

    if message.document:
        return DocumentMessageFormatter(message)
