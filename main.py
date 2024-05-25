import os
import discord
from discord.ext import commands

__VERSION__ = "0.0.1"
__AUTHOR__ = "hlc23"
__AUTHOR_ID__ = 595561546470653995
__EMAIL__ = "henryleecode23@gmail.com"

bot = commands.Bot(intents=discord.Intents.all(), test_guilds=[int(os.getenv("GUILD_ID"))])

bot.__VERSION__ = __VERSION__
bot.__AUTHOR__ = __AUTHOR__
bot.__AUTHOR_ID__ = __AUTHOR_ID__
bot.__EMAIL__ = __EMAIL__

bot.load_extension("cogs.basic")
bot.load_extension("cogs.error_handler")
bot.load_extension("cogs.cmd")

bot.run(os.getenv("TOKEN"))
