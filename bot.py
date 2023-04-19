import discord
from discord.ext import commands
import os, re
### env for token ###
from dotenv import load_dotenv
### Random Response ###
import random
### Date for Logging ###
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
bot = commands.Bot(command_prefix='!', intents=intents)


################## VARS ###############################################
### Production ###
initDate = datetime.datetime.now()
dateNow = initDate.strftime("%B-%d-%Y")
currentDate = datetime.datetime.now().date()

### @'s ###
bot_id=
clayton_at=

### Voice Channels ###
vc_anchorage=
vc_private=
vc_afkchannel = 

### Text Channels ###
tc_general_chat=
tc_bot_training=

### User IDs ###
andrei_id = 
ashley_id = 
brandon_id = 
brayden_id = 
chelsea_id = 
cristian_id = 
coleton_id = 
clayton_id = 
daniel_id = 
matt_id = 
tyler_id = 
will_id = 
### Role ID ###
r_bangers = 
r_brothers = 


birthDates = {
    datetime.date(1111, 1, 1): matt_id,
    datetime.date(): andrei_id,
    datetime.date(): r_brothers,
    datetime.date(): tyler_id,
    datetime.date(): brayden_id,
    datetime.date(): chelsea_id,
    datetime.date(): brandon_id,
    datetime.date(): cristian_id,
    datetime.date(): daniel_id,
    datetime.date(): will_id,
    datetime.date(): ashley_id
}

### Links ###
lnk_bangers = 

### Emojis ###
# Get new emotes by doing \:emoji_name:
em_gator=
em_happy_kirm=

yes_words = ["yes","yeah","yee","sure"]
no_words = ["no","na","nah","not really","no","work"]


@bot.event
async def birthdate_check():
    now = datetime.datetime.now().time()
    while True:
        if now.hour == 9: #and now.minute == 38:
            for date, person in birthDates.items():
                if currentDate == date.replace(datetime.datetime.now().year):
                   await bot.get_channel(tc_general_chat).send(f":birthday: Happy birthday <@{person}>! :birthday:")
        await asyncio.sleep(3600)

@bot.command()
async def kick(ctx, member: discord.Member=None):
        if member is None:
            member = ctx.message.author
            await member.edit(voice_channel = bot.get_channel(None))
        elif member is not None and ctx.message.author.id == brayden_id:
            await member.edit(voice_channel = bot.get_channel(None))
@bot.command(pass_context=True)
async def afk(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
        await member.edit(voice_channel = bot.get_channel(vc_afkchannel))
    elif member is not None and ctx.message.author.id == brayden_id:
        await member.edit(voice_channel = bot.get_channel(vc_afkchannel))
@bot.command(pass_context=True)
async def joined(ctx, *, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
        await ctx.send(f'{member} joined on {member.joined_at}')
    elif member is not None:
        await ctx.send(f'{member} joined on {member.joined_at}')

@bot.command(pass_context=True)
async def play(ctx, *playDate):
    if ctx.message.author.id == brayden_id:
        global play_date
        play_date = playDate
    return

@bot.command()
async def when(ctx):
    try:
        play_date
    except:
        await ctx.send(f'No Date Yet')
        return
    else:
        await ctx.send(f'{play_date}')
        return

@bot.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(bot))
    await birthdate_check()

@bot.event
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
    at_response = []

    if message.author == bot.user:
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

    await bot.process_commands(message)

### Bandgers Assemble ###

    if user_message.lower() == f"<@{r_bangers}>":
        await message.channel.send(f'{lnk_bangers}')
        return

### Remove Clayton ###<
@bot.event
async def on_voice_state_update(member, before, after):
    #### Checks if user is clayton_id and their before state was self_mute###
    ### Next make and not in afk channel ###
    #### You have to define bot.get_channel in this class underneath on_voice_state_update
    if member.id == clayton_id and after.self_mute and not before.channel == bot.get_channel(vc_afkchannel) and not after.channel == bot.get_channel(vc_afkchannel) and member.guild == bot.get_guild(209403061205073931):
        await asyncio.sleep(300)
        if member.id == clayton_id and after.self_mute and not before.channel == bot.get_channel(vc_afkchannel):
            # await bot.get_channel(tc_general_chat).send(f'Later Gator {em_gator} {em_happy_kirm} .')    #member = bot.get_member(clayton_id)
            await member.edit(voice_channel = bot.get_channel(vc_afkchannel))
            return
### Move Matt if he sits in AFK for more than an HR ###
    if after.channel == bot.get_channel(vc_afkchannel):
        await asyncio.sleep(3600)
        if after.channel == bot.get_channel(vc_afkchannel):
            await member.edit(voice_channel = bot.get_channel(None))
            print(f'{member.name} has been kicked.')
#Get client to Run using Token
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
