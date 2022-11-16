from dotenv import load_dotenv
load_dotenv()

import os
import discord
from discord import app_commands
from discord.ext import tasks
from dispander import dispand

intents = discord.Intents.default()
intents.message_content = True
# client = discord.Client(intents=discord.Intents.all())
client = discord.Client(intents=intents)
token = os.environ['TOKEN']
id = os.environ['ID']
guild=discord.Object(id)
channel_id = os.environ['CHANNEL_ID']
tree = app_commands.CommandTree(client)

@tasks.loop(seconds=10)
async def loop():
    await tree.sync(guild=guild)
@client.event
async def on_ready():
    await tree.sync(guild=guild)
    loop.start()

@tree.command(name='bookmark', description='メッセージリンクから情報取得・出力', guild=guild)
async def slash(ctx: discord.Interaction, url: str):
    link = url.split('/')
    server = client.get_guild(int(link[4]))
    print(server)
    channel = client.get_channel(int(link[5]))
    print(channel)
    message = await channel.fetch_message(int(link[6]))
    print(message)
    embed = discord.Embed(title=server, description=message.content)
    await ctx.response.send_message(embed=embed)

client.run(token)
