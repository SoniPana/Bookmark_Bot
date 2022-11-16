from dotenv import load_dotenv
load_dotenv()

import os
import datetime
import discord
from discord.commands import Option


bot = discord.Bot()
token = os.environ['TOKEN']
id = os.environ['ID']
channel_id = os.environ['CHANNEL_ID']

@bot.event
async def on_reaction_add(reaction, member):
    schannel = bot.get_channel(channel_id)
    if (reaction.emoji == '⭐') and (reaction.count >= 3):
        embed = discord.Embed(color = 15105570)
        embed.set_author(name = reaction.message.author.name, icon_url = reaction.message.author.avatar_url)
        embed.add_field(name = "Message Content", value = reaction.message.content)
        if len(reaction.message.attachments) > 0:
            embed.set_image(url = reaction.message.attachments[0].url)
        embed.set_footer(text = f" ⭐ {reaction.count} | # {reaction.message.channel.name}")
        embed.timestamp = datetime.datetime.utcnow()
        await schannel.send(embed = embed)

# @bot.slash_command(guild_ids=[id], description="退出")
# async def bookmark(ctx,
#                url: Option(str, 'URLを入力して下さい')
# ):
#     embed = discord.Embed(description = f'[test]({url})')
#     await ctx.respond(embed=embed)
#     await bot.close()

bot.run(token)
