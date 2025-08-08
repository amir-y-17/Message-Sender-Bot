# Message Sender Bot

A Python-based Telegram bot that automatically forwards new messages from a Telegram channel to an Eitaa channel using the official Eitaa API.  
Supports multiple content types including text, photos, videos, documents, and audio with captions.

---

## 📌 Features
- Fetches **new messages** from a specified Telegram channel.
- Formats different message types for Eitaa API compatibility.
- Sends:
  - Text messages
  - Photos with captions
  - Videos with captions
  - Documents
  - Audio / Music
- Uses the **official Eitaa API** for message delivery.

---

## 📦 Requirements
- **Python** 3.10 or higher
- **python-telegram-bot** (latest version)
- **Eitaa API Token** from the official Eitaayar website.

---

## ⚙️ Installation & Setup

1. **Create a Telegram Bot**  
   - Open [BotFather](https://t.me/BotFather) in Telegram.  
   - Use `/newbot` to create a new bot and get the bot token.

2. **Create a Python Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
   ```bash
   # Windows
   cd .venv\Scripts
   activate
   cd ../..

   # Linux/Mac
   source .venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create Environment Variables**
   - Inside the `config` folder, create a file named `.env`.
   - Add the following variables:
     ```env
     TOKEN=your_telegram_bot_token
     API_TOKEN=your_eitaa_api_token
     TELEGRAM_CHANNEL_ID=your_telegram_channel_chat_id
     EITAA_CHANNEL_ID=your_eitaa_channel_chat_id
     ```

6. **Run the Bot**
   ```bash
   python main.py
   ```

---

## 📂 Project Structure
```
MESSAGE-SENDER-BOT/
│
├── main.py
├── LICENSE
├── .gitignore
├── README.md
├── requirements.txt
│
├── bot/
│   ├── __init__.py
│   ├── telegram_client.py
│   └── handlers/
│       ├── __init__.py
│       ├── admin_handler.py
│       ├── channel_post_handlers.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── core/
│   ├── __init__.py
│   ├── channels.py
│   └── forward.py
│
├── storage/
│   ├── __init__.py
│   └── json_store.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│   ├── downloaders.py
│   ├── formatters.py
```

---

## 🔄 How It Works
1. The bot listens for **new messages** in your Telegram channel.  
2. Each message is processed and formatted based on its type (text, photo, video, etc.).  
3. The formatted message is sent to the **Eitaa API** with the given channel ID.  
4. The message appears in the target Eitaa channel.

**Flow Diagram**  
```
Telegram Channel → Message Sender Bot → Eitaa API → Eitaa Channel
```

---

## ⚠️ Notes
- The bot **must be an admin** in the Telegram channel to receive messages.
- Ensure your Eitaa API token is valid and has permission to send messages to the target channel.
- API rate limits may apply.

---

## 📄 License
This project is licensed under the **MIT License** — feel free to use and modify.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact
If you have any questions, feel free to open an issue or reach out via Telegram.
