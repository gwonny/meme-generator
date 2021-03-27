# bot.py

"""
STATE = {
    name: {
        img
        caption
    }
}
"""

import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
from img_utils import add_text

image_types = ["png", "jpg"]

# SET UP
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
STATE = {}
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

#Exit
@bot.command(help="disconnect bot")
async def exit(ctx):
    #Allow user to close bot from discord
    print('EXIT MESSAGE SENT')
    await bot.logout()

#Images
@bot.event
async def on_message(message):
    #Ignore bot messages, to prevent infinite loop
    if message.author.bot: return
    user_id = str(message.author.id)
    if user_id not in STATE: STATE[user_id] = {}
    filename = ''
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            filename = user_id + attachment.filename[-4:]
            await attachment.save(filename)

    if filename == '':
        await bot.process_commands(message)
        return
    STATE[user_id]['img'] = filename
    print(STATE)

#Memeify
@bot.command(help="generate your meme")
async def meme(ctx, *input_caption):
    user_id = str(ctx.message.author.id)

    # set caption
    caption = ' '.join(input_caption).strip()
    if not caption:
        # generate caption here
        pass

    if user_id not in STATE: STATE[user_id] = {}
    
    if 'img' not in STATE[user_id] or not STATE[user_id]['img']:
        ctx.message.channel.send("Input an image first")

    #Perform Memeify Function here
    add_text(STATE[user_id]['img'], caption, 50, STATE[user_id]['img'])
    await ctx.message.channel.send(file=discord.File(STATE[user_id]['img']))


bot.run(TOKEN)
