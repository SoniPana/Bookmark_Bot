# from dotenv import load_dotenv
# load_dotenv()

import os
import discord
from logging import getLogger, StreamHandler, DEBUG, Formatter
from discord import app_commands
from discord.ext import tasks


# Discordの設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# トークン、サーバーID、ログ設定
token = os.environ['TOKEN']
guild = discord.Object(os.environ['ID'])
logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = StreamHandler()
format = Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler.setFormatter(format)
logger.addHandler(handler)

@tasks.loop(seconds=10)
async def loop():
    await tree.sync(guild=guild)
@client.event
async def on_ready():
    await tree.sync(guild=guild)
    loop.start()
    logger.info('set up was finished.')

@tree.command(name='bookmark', description='見やすい', guild=guild)
@app_commands.describe(url='メッセージURL', title='タイトル', memo='メモ', color='色指定')
async def slash(ctx: discord.Interaction, url: str, title: str, memo: str=None, color: str=None):
    if color == None:
        color = 'default'
    embed = discord.Embed(title=title, url=url, description=memo, color=eval(f'discord.Colour.{color}')())
    await ctx.response.send_message(embed=embed)
    logger.info(f'sent message. ({title})')

@tree.command(name='help', description='ヘルプ', guild=guild)
async def slash(ctx: discord.Interaction):
    embed = discord.Embed(title='Bookmark_Bot', description='メッセージリンクを見やすくするBot', color=0xa6ccdd)
    color_li = ['red', 'dark_red', 'lighter_grey(gray)', 'dark_grey(gray)', 'light_grey(gray)', 'darker_grey(gray)', 'og_blurple', 'blurple', 'greyple', 'dark_theme', 'fuchsia', 'yellow']
    color = '\n'.join(color_li)
    embed.add_field(name='・colorで使用できる色', value=color)
    await ctx.response.send_message(embed=embed)
    logger.info(f'sent help message.')

client.run(token)
