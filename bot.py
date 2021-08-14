from discord.ext import commands
import discord
import os

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!")

def get_tag(tag: str) -> str:
    for file in os.listdir("./guides"):
        if file.strip(".md") == tag:
            return os.path.join("guides", file).read()
    
    return "failed to find tag!"


@bot.command()
async def tag(ctx, term: str):
    embed = discord.Embed(
        title=term,
        description=get_tag(tag)
    )

    await ctx.channel.send(embed=embed)

bot.run(TOKEN)