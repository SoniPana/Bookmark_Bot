from dotenv import load_dotenv
load_dotenv()

import os
import discord
from dispander import dispand, delete_dispand

client = discord.Client(intents=discord.Intents.all())
token = os.environ['TOKEN']
id = os.environ['ID']
channel_id = os.environ['CHANNEL_ID']

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await dispand(message)

@client.event
async def on_raw_reaction_add(payload):
    await delete_dispand(client, payload=payload)

client.run(token)
