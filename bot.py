import discord
# from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import json
import requests
import datetime

#### For Waiting ####
import asyncio

load_dotenv()
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.voice_states = True
intents.guilds = True
client = discord.Client(intents=intents)



# import discord

# intents = discord.Intents.all()

# client = discord.Client(intents=intents)

initDate = datetime.datetime.now()
dateNow = initDate.strftime("%B-%d-%Y")
# logDate = initDate.strftime("%Y-%m-%-d")
################## VARS ###############################################
### Production ###

### @'s ###
bot_id=""
clayton_at=""

### User IDs ###
brayden_id=
clayton_id=
daniel_id= #Daniel ID
matt_id=
### Text Channels ###
tc_afkchannel=
tc_general_chat=
tc_bot_training=

### Voice Channels ###
vc_anchorage=
vc_private=

### Emojis ###
# Get new emotes by doing \:emoji_name:
em_gator=""
em_happy_kirm=""
em_moffman=""


yes_words = ["yes","yeah","yee","sure"]
no_words = ["no","na","nah","not really","no","work"]


################################### Functions ###################################
@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    ### Gets UserName ###
    username = str(message.author).split('#')[0]
    ### Gets Message ###
    user_message = str(message.content)
    ### Get's Channel ###
    channel = str(message.channel.name)
    
    server_name = str(message.guild.name)

    nick = str(message.author.nick)
    ### Prints usernames and messages and channel for logging###
    print(f'{dateNow} | {server_name} | {username}: {user_message} | ({channel})')

    ### at_response variable###
    at_response = [f'response1','reponse2']

### Return if message is the bot ###
    if message.author == client.user:
        return
### Randomly responds with database choice from at_response
    if user_message.lower() == f'<{bot_id}>': # Bot @
        await message.channel.send(f'{random.choice(at_response)}')
        return

### Replies for scumgang channel ###
    if message.channel.name == 'scumgang':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username} {nick}!')
            return 
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Later Gator!')
            return
        elif user_message.lower() == '$human':
            quote = get_human_name
            await message.channel.send(quote)

### Remove Clayton ###
@client.event
async def on_voice_state_update(member, before, after):
    #### Checks if user is clayton_id and their before state was self_mute###
    ### Next make and not in afk channel ###
    #### You have to define client.get_channel in this class underneath on_voice_state_update
    if member.id == clayton_id and after.self_mute and not before.channel == client.get_channel(tc_afkchannel) and not after.channel == client.get_channel(tc_afkchannel) and member.guild == client.get_guild(209403061205073931):
        await asyncio.sleep(300)
        if member.id == clayton_id and after.self_mute and not before.channel == client.get_channel(tc_afkchannel):
            await client.get_channel(tc_general_chat).send(f'Later Gator {em_gator} {em_happy_kirm} .')    #member = client.get_member(clayton_id)
            await member.edit(voice_channel = client.get_channel(tc_afkchannel))
            return
    if member.id == matt_id and after.channel == client.get_channel(tc_afkchannel):
        print(f'Matt has been disconnected.')
        await asyncio.sleep(3600)
        await member.edit(voice_channel = client.get_channel(None))
        await client.get_channel(tc_general_chat).send(f'Bye-Bye Moffman! {em_moffman}')



#Get client to Run using Token
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
