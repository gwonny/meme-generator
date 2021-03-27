# bot.py
import os
import random

import discord
from dotenv import load_dotenv

image_types = ["png", "jpg"]

counter = 0

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: discord.Message):
    #Ignore bot messages, to prevent infinite loop
    if message.author.bot: return
    
    #
    if message.content == "exit":
        await client.logout()
    
    response = message.content
    counter = str(random.randint(0,100000))
    filename = ''
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            filename = counter + attachment.filename[-4:]
            await attachment.save(filename)

    if filename == '': return
    #Do work on images
    #Modify Image
    if (response == ''): response = 'When you nut but she keeps sucking'
    #response = generateResponse(response)
    #createPhoto(response)
    await message.channel.send(file=discord.File(filename))

    os.remove(filename)

client.run(TOKEN)
