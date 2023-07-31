import discord
from discord.ext import commands
from dotenv import load_dotenv
from colorama import Fore
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

# Colors
RED = 0x990000
GREEN = 0x013220

print(Fore.GREEN + "============================" + Fore.RESET)
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename[:-3]}")


@bot.event
async def on_ready():
    print(f"Using: {bot.user}")
    print(f"I Am on {len(bot.guilds)} Server(s)")
    print(Fore.GREEN + "============================" + Fore.RESET)


# Cog management
@bot.slash_command()
async def unload(ctx, cog):
    if ctx.author.id == 1114012186877120643:
        cog = "cogs." + cog
        bot.unload_extension(cog)
        await ctx.respond(f"Unloaded {cog}")
    else:
        await ctx.respond("No")


@bot.slash_command()
async def load(ctx, cog):
    if ctx.author.id == 1114012186877120643:
        cog = "cogs." + cog
        bot.load_extension(cog)
        await ctx.respond(f"Loaded {cog}")
    else:
        await ctx.respond("No")


@bot.slash_command()
async def reload(ctx, cog):
    if ctx.author.id == 1114012186877120643:
        cog = "cogs." + cog
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await ctx.respond(f"Reloaded {cog}")
    else:
        await ctx.respond("No")


bot.run(TOKEN)
