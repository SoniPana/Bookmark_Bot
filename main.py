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
@app_commands.describe(url='メッセージURL', memo='メモ', color='色指定')
async def slash(ctx: discord.Interaction, url: str, memo: str=None, color: str=None):
    link = url.split('/')
    server = client.get_guild(int(link[4]))
    print(f'{link[4]},{server}')
    channel = client.get_channel(int(link[5]))
    print(f'{link[5]},{channel}')
    message = await channel.fetch_message(int(link[6]))
    print(message)
    author = await client.fetch_user(message.author.id)
    print(author.avatar.url)
    if color == None:
        color = 'default'
    embed = discord.Embed(title=server, description=message.content, color=eval(f'discord.Colour.{color}')())
    embed.set_author(name=author, url=url, icon_url=author.avatar.url)
    await ctx.response.send_message(embed=embed)

@tree.command(name='help', description='ヘルプ', guild=guild)
async def slash(ctx: discord.Interaction):
    embed = discord.Embed(title='Bookmark_Bot', description='作成中', color=0xa6ccdd)
    await ctx.response.send_message(embed=embed)

client.run(token)
