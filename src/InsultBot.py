import os

import discord
from dotenv import load_dotenv
import random_insult_reader

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
intents = discord.Intents(messages=True, guilds=True)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send(random_insult_reader.biggie_string)

client.run(TOKEN)
