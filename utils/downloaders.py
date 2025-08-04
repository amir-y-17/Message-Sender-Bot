import os
import requests
from config.settings import *


def download_telegram_file(file_id: str):
    try:
        file_info_url = f"https://api.telegram.org/bot{TOKEN}/getFile"
        response = requests.get(file_info_url, params={"file_id": file_id}, timeout=10)

        # Check the response status
        response.raise_for_status()
        data = response.json()

        if not data.get("ok") or "result" not in data:
            raise ValueError(f"Invalid response structure: {data}")

        file_path = data["result"].get("file_path")
        if not file_path:
            raise ValueError("File path not found in response.")

        filename = os.path.basename(file_path)
        file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

        # Download the file
        file_response = requests.get(file_url, timeout=30)
        file_response.raise_for_status()

        os.makedirs("downloads", exist_ok=True)
        full_path = os.path.join("downloads", filename)

        with open(full_path, "wb") as f:
            f.write(file_response.content)

        return file_response.content, full_path

    except requests.exceptions.RequestException as e:
        print(f"[Download Error] Network issue: {e}")
    except (ValueError, KeyError) as e:
        print(f"[Download Error] Invalid response or missing data: {e}")
    except Exception as e:
        print(f"[Download Error] Unexpected error: {e}")

    return None, None
