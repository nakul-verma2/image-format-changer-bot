# 🖼️ Telegram Image Format Converter Bot

🚀 **Telegram Bot for Image Format Conversion** using the Telethon library and PIL (Pillow) 🧑‍💻. This bot allows users to easily convert images between various formats directly within Telegram!

## ✨ Features
- 🌟 **Supports multiple image formats:** JPEG, JPG, PNG, and WEBP.
- 📥 **Effortless Image Upload:** Users can send images directly to the bot, which will automatically handle the conversion.
- 📲 **Interactive UI:** The bot provides a user-friendly interface with buttons to start the conversion process.
- 🔄 **Automated Conversion Process:** The bot checks the format of the uploaded image and guides the user to select the desired output format.
- ✅ **Error handling:** Provides feedback on unsupported formats and failed conversions.

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nakul-verma2/image-format-changer-bot
   ```
2. Open Folder:
   ```bash
   cd image-format-changer-bot
   ```
3. Create a image folder inside repo:
   ```bash
   mkdir image
   ```
4. Create a virtual environment:
   ```bash
   python3 -m venv myenv && source myenv/bin/activate
   ```
5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Edit your bot token, api_id, and api_hash in the script bot.py:
   
   ```python
   bot_token = "your-bot-token"
   api_id = "your-api-id"
   api_hash = "your-api-hash"
   ```
   
7. Run the bot:
   
   ```bash
   python3 bot.py
   ```

## ⚙️ Usage
- Send `/start` to begin interacting with the bot.
- Upload an image and select the format you want to convert it to.
- The bot will send you the converted image in the format of your choice!

## 🔧 Supported Formats
- JPEG
- JPG
- PNG
- WEBP

## 🤖 Technologies Used
- [Telethon](https://github.com/LonamiWebs/Telethon): For interacting with the Telegram API.
- [Pillow (PIL)](https://pillow.readthedocs.io/): For image processing.

## 💬 Commands
- `/start`: Begin interaction with the bot.
- `/Help`: Provides information on supported formats and usage instructions.
- `/Change Format Of An Image`: Convert images to another format.

## 🎉 Contributing
Feel free to open issues or submit pull requests to enhance the functionality of the bot.

## 📜 License
This project is licensed under the MIT [License](https://github.com/nakul-verma2/image-format-changer-bot/blob/main/LICENSE).
