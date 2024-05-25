import os
import discord
from discord.ext import commands

class CmdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # make a shell
    @commands.slash_command()
    @commands.has_role(1132919955172626452)
    async def system(self, ctx: discord.ApplicationContext, cmd: str):
        await ctx.respond(os.popen(cmd).read(), ephemeral=True)

    @commands.slash_command()
    @commands.has_role(1132919955172626452)
    async def reset_target(self, ctx: discord.ApplicationContext):
        try:
            os.system("vboxmanage controlvm mv reset")
        except Exception as e:
            ctx.respond(f"An error occurred: {e}", ephemeral=True)
        else:
            ctx.respond("Target machine restarting, try connect later.", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(CmdCog(bot))
