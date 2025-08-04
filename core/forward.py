import os
import requests
import mimetypes
from abc import ABC, abstractmethod
from utils.downloaders import download_telegram_file


class BaseForwarder(ABC):
    def __init__(self, api_url: str):
        self.api_url = api_url

    @abstractmethod
    def forward(self, data: dict):
        pass


class TextForwarder(BaseForwarder):
    def forward(self, data: dict):
        URL = self.api_url
        response = requests.post(URL, params=data)

        result = response.json()
        if result.get("ok", False):
            return 200, result
        else:
            return None


class FileForwarder(BaseForwarder):
    def forward(self, data: dict):
        file_bytes, full_path = download_telegram_file(data["file_id"])

        if not file_bytes or not full_path:
            return 400, "Failed to download file from Telegram."

        try:
            mime_type, _ = mimetypes.guess_type(full_path)
            if not mime_type:
                mime_type = "application/octet-stream"

            filename = os.path.basename(full_path)
            files = {"file": (filename, file_bytes, mime_type)}

            response = requests.post(self.api_url, data=data, files=files)
            response.raise_for_status()

            result = response.json()
            if result.get("ok", False):
                return 200, result
            else:
                return 400, result.get("description", "Unknown error")

        except requests.RequestException as e:
            return 500, f"API request failed: {str(e)}"

        finally:
            if full_path and os.path.exists(full_path):
                os.remove(full_path)


def get_forwarder(message_type: str, api_url: str):
    if message_type == "text":
        return TextForwarder(api_url)

    if message_type == "file":
        return FileForwarder(api_url)

    return None
