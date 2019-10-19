import os
import discord
import bot_log
import bot_creds
from dotenv import load_dotenv
load_dotenv()


TOKEN = bot_creds.token
bot_chan_id = 635202004058243117


client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg_chan_id = message.channel.id
    bot_channel = message.guild.get_channel(bot_chan_id)
    if(msg_chan_id == bot_chan_id):
        ##simple response to user when they speak in whichever channel they speak
        at_user = message.author.mention
        await bot_channel.send(
            f"Hello {at_user} this is my channel."
        )

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord!")

client.run(TOKEN)
