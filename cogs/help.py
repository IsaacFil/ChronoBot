from discord.ext import commands
from discord.commands import slash_command
import discord


class HelpCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def help(ctx, page: discord.Option(str, choices=[1])):
        embed = discord.Embed(title="Bot commands", color=0x008B8B)
        if choices == 1:
            embed.add_field(name="help", value="Shows you this")
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
