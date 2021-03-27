# bot.py
import os
import random

import discord
from dotenv import load_dotenv

image_types = ["png", "jpeg", "gif", "jpg"]

counter = 0

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
    
    response = message.content
    #counter = random.randint(0,10000)
    found = False
    filename = ""
    #response = "hi"
    #await message.channel.send(response)
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            filename = attachment.filename
            await attachment.save(filename)
            found = True

    if not found: return
    #Save Attachment
    #Do work on images
    #Modify Image
    if (response == ""): response = 'When you nut but she keeps sucking'

    
    
    await message.channel.send(file=discord.File(filename))

client.run(TOKEN)
