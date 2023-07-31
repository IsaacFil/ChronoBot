import discord
from discord.ext import commands
from datetime import datetime


class ErrorHandler(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title=f"<:error:1135563101689888799> An error occured",
                description=f"`{error}`",
                color=RED,
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title=f"<:error:1135563101689888799> An error occured",
                description=f"`{error}`",
                color=RED,
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title=f"<:error:1135563101689888799> An error occured",
                description=f"`{error}`",
                color=RED,
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
