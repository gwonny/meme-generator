# bot.py
import os

import discord
from dotenv import load_dotenv

image_types = ["png", "jpeg", "gif", "jpg"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: discord.Message):
    if message.author.bot: return
    if message.content == "exit":
        await client.logout()
    
    #response = "hi"
    #await message.channel.send(response)
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            await attachment.save(attachment.filename)

    #Save Attachment
    #Do work on images
    #Modify Image


client.run(TOKEN)
