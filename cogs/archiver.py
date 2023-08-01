from discord.ext import commands
from discord.commands import slash_command
import discord
from discord import File
from os import linesep
import io
import os
from datetime import datetime


class Archiver(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def archive(
        self,
        ctx,
        channel: discord.TextChannel,
        sortby: discord.Option(str, choices=["Oldest To Newest", "Newest To Oldest"]),
        limit: int = 100000,
        ignore_bot: bool = True,
    ):
        if channel == None:
            embed = discord.Embed(
                title=f"<:error:1135563101689888799> An error occured",
                description=f"`Missing argument (channel)`",
                color=RED,
            )
            await ctx.respond(embed=embed)
        await ctx.respond("Archiving... (may take a minute)")
        # messages = await channel.history(limit=1).flatten()
        msg_list = []
        async for message in channel.history(limit=limit):
            if ignore_bot:
                if not message.author.bot:
                    msg_author = message.author
                    msg_author_id = message.author.id
                    msg_content = message.content
                    msg_time = message.created_at
                    msg_time = msg_time.strftime("%m/%d/%y, %H:%M")
                    try:
                        if message.content.Embed:
                            msg_content = f"{msg_content}\n(Embed)\n[Title: {message.Embed.title}]\nDescription: {message.Embed.description}"
                    except Exception:
                        pass
                    msg = (
                        f"[{msg_time}]({msg_author_id})--\n{msg_author}: {msg_content}"
                    )
                    msg_list.append(msg)
            else:
                msg_author = message.author
                msg_author_id = message.author.id
                msg_content = message.content
                msg_time = message.created_at
                msg_time = msg_time.strftime("%m/%d/%y, %H:%M")
                try:
                    if message.content.Embed:
                        msg_content = f"{msg_content}\n(Embed)\n[Title: {message.Embed.title}]\nDescription: {message.Embed.description}"
                except Exception:
                    pass
                msg = f"[{msg_time}]({msg_author_id})--\n{msg_author}: {msg_content}"
                msg_list.append(msg)
        if sortby == "Oldest To Newest":
            file = io.StringIO(linesep.join(msg_list[::-1]))
            await ctx.edit(
                content=f"Done! ({sortby})",
                file=File(fp=file, filename=f"{channel}-archive.txt"),
            )
        if sortby == "Newest To Oldest":
            file = io.StringIO(linesep.join(msg_list))
            await ctx.edit(
                content=f"Done! ({sortby})",
                file=File(fp=file, filename=f"{channel}-archive.txt"),
            )


def setup(bot):
    bot.add_cog(Archiver(bot))
