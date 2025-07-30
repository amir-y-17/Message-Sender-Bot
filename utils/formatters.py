# Base class
class MessageFormatter:
    def __init__(self, message):
        self.message = message

    def format(self) -> dict:
        pass


# Formatter subclasses
class TextMessageFormatter(MessageFormatter):
    def format(self) -> dict:
        data = {"text": self.message.text}
        return data


class PhotoMessageFormatter(MessageFormatter):
    def format(self) -> dict:
        pass


class VideoMessageFormatter(MessageFormatter):
    def format(self) -> dict:
        pass


class AudioMessageFormatter(MessageFormatter):
    def format(self) -> dict:
        pass


class VoiceMessageFormatter(MessageFormatter):
    def format(self) -> dict:
        pass


class DocumentMessageFormatter(MessageFormatter):
    def format(self):
        pass


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
