from telethon import TelegramClient, events, Button
from PIL import Image
import os

SUPPORTED_FORMATS = ["jpeg", "jpg", "png", "webp"]
bot_token = "your-bot-token"
api_id = "your-api-id"
api_hash = "your-api-hash"

bot = TelegramClient('bot', api_id=api_id, api_hash=api_hash).start(bot_token=bot_token)

user_states = {}

async def cf(event, file_path, output_format):
    try:
        if output_format not in SUPPORTED_FORMATS:
            await event.reply(f"Error: {output_format} format is not supported. Please choose from {SUPPORTED_FORMATS}.")
            return  

        with Image.open(file_path) as img:
            file_name, _ = os.path.splitext(file_path)

            if output_format == "jpeg":
                output_image_path = f"{file_name}.jpeg"
                img.save(output_image_path, format="JPEG")
            elif output_format == "jpg":
                output_image_path = f"{file_name}.jpg"
                img.save(output_image_path, format="JPEG")
            else:
                output_image_path = f"{file_name}.{output_format.lower()}"
                img.save(output_image_path, format=output_format.upper())

            await event.reply(f"Image successfully converted to {output_format} format. Sending you the converted image...")
            await event.reply(file=output_image_path)
            #os.remove(output_image_path)

    except FileNotFoundError:
        await event.reply("Error: The input image file was not found.")
    except OSError as e:
        await event.reply(f"Error: Unable to convert the image. Reason: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    user = await event.get_sender()
    user_id = user.id
    username = user.username
    phone = user.phone

    message = f"""
    **Welcome To Image Editor!** 🎉
    
    You are interacting with the bot:-
    
    - **User ID:** `{user_id}`
    - **Username:** @{username if username else "Not set"}
    - **Phone Number:** {phone if phone else "Not available"}
    """
    
    
    await event.respond(
        message,
        buttons=[
            [Button.text("/Change Format Of An Image")],
            [Button.text("/Help")]
        ],
        parse_mode='markdown',
    )
    await event.respond("**🌟Hi! File Converter is at your service!🌟**\n\nWith me you can convert files from one format to another.\n\n📷 Images and other files are supported.\n🔗 Images as docment are supported too.\n\nSend me a file to convert or type /Help for more information.")
@bot.on(events.NewMessage(pattern='/Help'))
async def change_format(event):
    await event.respond("**❇️Send me a file to convert.❇️**\n\n**🔱4 Supported files 🔱:**\n\n📷 Images\n__JPEG, JPG, PNG, WEBP__")


@bot.on(events.NewMessage(pattern='/Change Format Of An Image'))
async def change_format(event):
    await event.respond("**🔰Send me the image format you want to convert.🔰**")

@bot.on(events.NewMessage)
async def handle_image(event):
    if event.message.message.startswith('/'):
        return

    if event.photo or (event.document and event.document.mime_type.startswith('image/')):
        download_msg = await event.reply("Downloading the image to check format\n□□□□□□□□□□")
        await download_msg.edit("Downloading the image to check format\n▪□□□□□□□□□")
        await download_msg.edit("Downloading the image to check format\n▪▪□□□□□□□□")
        await download_msg.edit("Downloading the image to check format\n▪▪▪□□□□□□□")
        await download_msg.edit("Downloading the image to check format\n▪▪▪▪□□□□□□")
        await download_msg.edit("Downloading the image to check format\n▪▪▪▪▪□□□□")
        await download_msg.edit("Downloading the image to check format\n▪▪▪▪▪▪□□□")
        await download_msg.edit("Downloading the image to check format\n▪▪▪▪▪▪▪□□")
        await download_msg.edit("Downloading the image to check format\n▪▪▪▪▪▪▪▪□")
        await download_msg.edit("Downloading the image to check format\n▪▪▪▪▪▪▪▪▪")

        file_path = await event.download_media(file='image/')

        if file_path.lower().endswith(('.heic', '.heif')):
            await download_msg.edit("HEIC/HEIF format is not supported. Please upload a jpeg, jpg, png, or webp image.")
            os.remove(file_path)
            return
        
        try:
            image = Image.open(file_path)
            if image.format.lower() in SUPPORTED_FORMATS:
                await download_msg.edit("Format is supported. Proceeding with Conversion...")
                await event.reply(
                    "Choose a format for conversion:",
                    buttons=[
                        [Button.text("JPEG"), Button.text("JPG")],
                        [Button.text("PNG"), Button.text("WEBP")]
                    ]
                )
                user_states[event.sender_id] = file_path
            else:
                await event.reply("Unsupported format. Please upload a jpeg, jpg, png, or webp image.")
                os.remove(file_path)

        except Exception as e:
            await event.reply(f"Error opening the image: {str(e)}")
            os.remove(file_path)

        return

    if event.message.text and event.sender_id in user_states:
        output_format = event.raw_text.lower()
        if output_format in SUPPORTED_FORMATS:
            await event.reply(f"Converting to {output_format}...")
            converting_msg= await event.reply("Format is supported. Proceeding with Conversion\n□□□□□□□□□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪□□□□□□□□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪□□□□□□□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪▪□□□□□□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪▪▪□□□□□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪▪▪▪□□□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪▪▪▪▪□□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪▪▪▪▪▪□□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪▪▪▪▪▪▪□")
            await converting_msg.edit("Format is supported. Proceeding with Conversion\n▪▪▪▪▪▪▪▪▪")
            
            await cf(event, user_states[event.sender_id], output_format)
            del user_states[event.sender_id]
            await event.respond(
                "Have a nice day! 😊",
                buttons=[
                    [Button.text("/Change Format Of An Image")],
                    [Button.text("/Help")]
                ],
                parse_mode='markdown',
            )
        else:
            await event.reply(f"Error: {output_format} is not a supported format. Please choose from {SUPPORTED_FORMATS}.")

print("Bot is running...")
bot.run_until_disconnected()
