# Meme Generator Bot for Discord

A Discord bot built with Python 3 that captions memes given an image.

## Creating your own instance of the bot

1. Make sure you have the contents of this repository by cloning

```
$ git clone https://github.com/gwonny/meme-generator.git
```

2. Create your own bot account and invite the bot to your server (refer to the [Discord documentation](https://discordpy.readthedocs.io/en/latest/discord.html) for specific instructions)

3. At [discord.com/developers/applications](https://discord.com/developers/applications), click on your new bot/application

4. Under Settings, click on Bot

5. Copy the bot token

6. Create a `.env` file and include the following content:

```
# .env
DISCORD_TOKEN={place bot token here}
```

7. Install dependencies with

```
$ pip3 install -r requirements.txt
```

8. Run `bot.py`

## Inviting the bot to your server

1. If you have your own instance of the bot: </br>
   a. At [discord.com/developers/applications](https://discord.com/developers/applications), select your bot </br>
   b. Click the OAuth2 tab </br>
   c. Check the box labeled 'bot' in scopes, and check the box labeled 'Administrator' in bot permissions <br>
   d. Click the Discord authorization link at the bottom of scopes to invite the bot

2. If you want to invite our bot to your server: </br>
   a. Go to [this link](https://discord.com/api/oauth2/authorize?client_id=825185047321509929&permissions=8&scope=bot) </br>
   b. Select the server that you want to add the bot to

## Usage

1. Make sure you have invited the bot to your server using the instructions in **Inviting the bot to your server**
2. To have the bot caption your image, first upload a `jpg` or `png` image
3. Use `!meme <top caption> | <bottom caption> | !color:<text color>` to generate captions for your image. Any of the 3 arguments in the `!meme` command can be omitted.
