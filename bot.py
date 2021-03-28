# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
from img_utils import add_text, find_color_text
from essential_generators import DocumentGenerator

image_types = ["png", "jpg"]

# SET UP
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
STATE = {}
gen = DocumentGenerator()
"""
STATE = {
    name: {
        img
    }
}
"""

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

#Exit
@bot.command(help="disconnect bot")
async def exit(ctx):
    #Allow user to close bot from discord
    await bot.logout()

#Images
@bot.event
async def on_message(message):
    #Ignore bot messages, to prevent infinite loop
    if message.author.bot: return

    # set user ID in state if it doesn't already exist
    user_id = str(message.author.id)
    if user_id not in STATE: STATE[user_id] = {}

    # check that the message has an attachment and that the attachment is a jpg or png
    filename = ''
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            filename = user_id + attachment.filename[-4:]
            await attachment.save(filename)

    if filename == '':
        await bot.process_commands(message)
        return
    STATE[user_id]['img'] = filename

#Memeify
@bot.command(help="!meme <top caption> | <bottom caption> | !color:<text color>")
async def meme(ctx, *input_caption):
    user_id = str(ctx.message.author.id)

    if 'img' not in STATE[user_id] or not STATE[user_id]['img']:
        await ctx.message.channel.send("Upload a jpg or png image first")
        return

    # set caption
    caption = ' '.join(input_caption).strip()
    if not caption:
        caption = gen.sentence()
    
    # parse caption
    texts = caption.split('|')
    color = 'white'
    bottom = ''
    
    if '!color:' in caption:
        color = find_color_text(caption, '!color:', 'white')
        texts.pop()

    if len(texts) == 2:
        bottom = texts[1]
    if len(texts) >= 1:
        top = texts[0]
    if len(texts) == 0:
        top = gen.sentence()

    if user_id not in STATE: STATE[user_id] = {}
    
    file_name = STATE[user_id]['img']
    file_type = file_name[-4:]
    modified_file_name = file_name[:-4] + "_modified" + file_type
    
    #Perform Memeify Function here
    add_text(file_name, caption, 50, modified_file_name, top, bottom, color)
    await ctx.message.channel.send(file=discord.File(modified_file_name))
    os.remove(modified_file_name)


bot.run(TOKEN)
