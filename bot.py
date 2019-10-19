import os
import discord
import bot_log
import bot_creds

TOKEN = bot_creds.token
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    bot_channel = message.channel
    print(bot_channel)
    