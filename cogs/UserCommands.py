from discord.ext import commands


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="HelloWorld")
    async def hello_world_command(self, ctx):
        await ctx.channel.send("Hello world")


def setup(bot):
    bot.add_cog(UserCommands(bot))
