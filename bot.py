from pydoc import cli
import discord
import os
from dotenv import load_dotenv
import random
import json
import requests

load_dotenv()
bot = discord.Client()
client = discord.Client()

yes_words = ["yes","yeah","yee","sure"]
no_words = ["no","na","nah","not really","no","work"]

bot_id="redacted"


def get_human_name ():
    reponse = requests.get("htimport ostps://www.fantasynamegenerators.com/dnd-human-names.php")
    json_data = json.loads(response.text)
    human_name = json_data

###ideas (yes / no tracker )for if they want to play, name generator)  



@client.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    at_response = [f'Gods angels strike {username} in the face.',f'Fuck off Mate.']

    if message.author == client.user:
        return
    # if user_message.lower() == '!random': # Bot @  unsure
    #     await message.channel.send(f'{random.choice()}')
    #     return
    if user_message.lower() == f'<{bot_id}>': # Bot @
        await message.channel.send(f'{random.choice(at_response)}')
        return

    if message.channel.name == 'scumgang':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return 
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Later Gator!')
            return
        elif user_message.lower() == '$human':
            quote = get_human_name
            await message.channel.send(quote)
 

#Get client to Run using Token
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)