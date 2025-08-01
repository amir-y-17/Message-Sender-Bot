import os
import requests
from config.settings import *


def download_telegram_file(file_id: str):
    # Get file information
    file_info_url = f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}"
    response = requests.get(file_info_url)
    response.raise_for_status()

    file_path = response.json()["result"]["file_path"]
    filename = file_path.split("/")[-1]

    # Build the file download URL
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    file_response = requests.get(file_url)
    file_response.raise_for_status()

    # Create downloads/ directory if it doesn't exist
    os.makedirs("downloads", exist_ok=True)
    full_path = os.path.join("downloads", filename)

    # Write the file to disk
    with open(full_path, "wb") as f:
        f.write(file_response.content)

    return file_response.content, full_path
