import discord
from discord.ext.commands import errors
from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
        if isinstance(error, errors.MissingRole):
            await ctx.respond("You don't have the required role to run this command!", ephemeral=True)
        else:
            await ctx.respond(f"An error occurred: {error}", ephemeral=True)
            dm = await self.bot.create_dm(self.bot.get_user(self.bot.__AUTHOR_ID__))
            if ctx.guild == None:
                await dm.send(f"An error occurred in {ctx.author.display_name}'s channel ({ctx.author.id}): {error}")
            else:
                await dm.send(f"An error occurred in {ctx.guild.name} ({ctx.guild.id}): {error}")
            await dm.send(f"Command: {ctx.command.name}")
            await dm.send(f"User: {ctx.author.name} ({ctx.author.id})")

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))