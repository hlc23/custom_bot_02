import discord
from discord.ext import commands

class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")
        print("Logged in as: ", self.bot.user.name)

    @commands.slash_command()
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond("Hello!")

    @commands.slash_command()
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"Pong! ({self.bot.latency * 1000:.0f}ms)")

def setup(bot: commands.Bot):
    bot.add_cog(BasicCog(bot))
