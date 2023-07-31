import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import File
from os import linesep
import io
import os 
from colorama import Fore
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = discord.Bot(command_prefix="c!", intents=intents)

# Colors
RED = 0x990000
GREEN = 0x013220

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title=f"<:error:1135563101689888799> An error occured", description=f"`{error}`", color=RED)
        await ctx.send(embed=embed)
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title=f"<:error:1135563101689888799> An error occured", description=f"`{error}`", color=RED)
        await ctx.send(embed=embed)
@bot.event
async def on_ready():
    print(Fore.GREEN + "============================" + Fore.RESET)
    print(f"Using: {bot.user}")
    print(f"I Am on {len(bot.guilds)} Server(s)")
    print(Fore.GREEN + "============================" + Fore.RESET)

@bot.command()
async def archive(ctx, channel: discord.TextChannel, limit: int = 200, ignore_bot: bool = True):
    if channel == None:
        embed = discord.Embed(title=f"<:error:1135563101689888799> An error occured", description=f"`Missing argument (channel)`", color=RED)
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
                try:
                    if message.content.Embed:
                        msg_content = f"{msg_content}\n(Embed)\n[Title: {message.Embed.title}]\nDescription: {message.Embed.description}"
                except Exception:
                    pass
        else:
            msg_author = message.author
            msg_author_id = message.author.id
            msg_content = message.content
            try:
                if message.content.Embed:
                    msg_content = f"{msg_content}\n(Embed)\n[Title: {message.Embed.title}]\nDescription: {message.Embed.description}"
            except Exception:
                pass
        msg_time = message.created_at
        msg_time = msg_time.strftime("%m/%d/%y, %H:%M")
        msg = f"[{msg_time}]({msg_author_id})--\n{msg_author}: {msg_content}"
        msg_list.append(msg)
    file = io.StringIO(linesep.join(msg_list[::-1]))
    await ctx.edit(content=f'Done! (Oldest to newest)', file=File(fp=file, filename=f"{channel}-archive.txt"))

bot.run(TOKEN)