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


bot.run(TOKEN)
