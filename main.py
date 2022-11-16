from dotenv import load_dotenv
load_dotenv()

import os
import discord
# from dispander import dispand
from discord.commands import Option


bot = discord.Bot()
bot.load_extension('dispander')
token = os.environ['TOKEN']
id = os.environ['ID']
channel_id = os.environ['CHANNEL_ID']

@bot.slash_command(guild_ids=[id], description="退出")
async def bookmark(ctx,
               url: Option(str, 'URLを入力して下さい')
):
    # embed = discord.Embed(description = f'[test]({url})')
    # await ctx.respond(embed=embed)
    await ctx.respond(url)
    await bot.close()

bot.run(token)
