import os
import random
import discord
import bot_log
import bot_creds
import datetime
from dotenv import load_dotenv
load_dotenv()

#TODO add oAuth to allow validation of multiple servers
#make fn time_check to optimize

TOKEN = bot_creds.token
GUILD =""
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
def hour_min_sec(secs):
    #thank you evan!
    return(int(secs//3600),int((secs%3600) //60), int(secs % 60))

@client.event
async def on_message(message):
    if(message.author.id == 78674342103224320):
        if(("quit" in message.content or "bye" in message.content) and
        message.channel.name == "bot-test"):
            await client.close()  

@client.event
async def on_ready():
    print(f"{client.user.name} has connected to discord!")
    for guild in client.guilds:
        if(guild.name == "Creative 747"):
            GUILD = guild
            break
    for user in GUILD.members:
        '''
        Check each user and check what type of activity they're doing, if it's a game
        we start our time mind
        '''
        if(user.activity):
            if(user.activity.type.name == "playing"):
                start_time = user.activity.timestamps["start"]/1000
                start_time = datetime.datetime.fromtimestamp(start_time)
                now = datetime.datetime.now()
                delt = now - start_time #a time delta object (days,s,ms)
                hour, mins, secs = hour_min_sec(delt.total_seconds())
                print(f'''{user.name} has been playing {user.activity.name} for {hour} hour(s) {mins}
                mins and {secs} secs.''')
                if(hour>3):
                    print(f"Hi {user.name}! "+random.choice(bot_creds.well)) ##TODO change this to user.message(content="")
client.run(TOKEN)
