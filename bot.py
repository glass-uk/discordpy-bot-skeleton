import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix=';', case_insensitive=True)

bot.load_extension("cogs.UserCommands")


@bot.command(hidden=True)
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0x89cff0)
    await ctx.send(embed=embed)


load_dotenv()
bot.run(os.getenv('LIVE_BOT'))
