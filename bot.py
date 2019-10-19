import os
import discord
import bot_log
import bot_creds
from dotenv import load_dotenv
load_dotenv()


TOKEN = bot_creds.token

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    bot_channel = message.channel
    print(bot_channel)
    to_user = message.author
    print(to_user)
    if(message.channel == bot_channel):
        at_user = message.author.mention
        await bot_channel.send(
            f"Hello @{at_user} ."
        )

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord!")

client.run(TOKEN)
