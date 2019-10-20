import os
import discord
import bot_log
import bot_creds
from dotenv import load_dotenv
load_dotenv()

TOKEN = bot_creds.token
bot_chan_id = bot_creds.bot_chan_id

client = discord.Client()

@client.event ##logging information pulled from realpython.com
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
'''
orphaned code, used for testing purpouses
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
'''

@client.event
async def on_message(message):
    if(message.author.id == 78674342103224320):
        if message.author == client.user:
            return
        if(("quit" in message.content or "bye" in message.content) and
        message.channel.name == "bot-test"):
            exit()


@client.event
async def on_ready():
    print(f"{client.user.name} has connected to discord!")


client.run(TOKEN)
