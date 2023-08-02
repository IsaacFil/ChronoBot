import httpx

# from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from discord.commands import slash_command
import psutil
import time

# load_dotenv("../.env")
# PTERO_KEY = os.getenv("API_TOKEN")


class Sys_info(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="system", description="Shows system info and performance")
    async def system(self, ctx):
        await ctx.defer()
        cpu_percentages = psutil.cpu_percent()
        cpu_max_percent = psutil.cpu_count() * 100
        cpu_usage_str = f"{cpu_percentages}" + f"/{cpu_max_percent:.2f}"

        memory = psutil.virtual_memory()
        ram_usage = memory.percent
        ram_max_percent = 100
        ram_usage_str = f"{ram_usage:.2f}/{ram_max_percent:.2f}"

        network_before = psutil.net_io_counters()
        time.sleep(1)  # Wait for a second
        network_after = psutil.net_io_counters()

        bytes_sent = network_after.bytes_sent - network_before.bytes_sent
        bytes_received = network_after.bytes_recv - network_before.bytes_recv

        upload_speed = bytes_sent / 1024 / 1024  # Convert to MB/s
        download_speed = bytes_received / 1024 / 1024  # Convert to MB/s

        embed = discord.Embed(title="Bot system resource usage", color=0x008B8B)
        embed.add_field(name="CPU Usage", value=f"{cpu_usage_str}%")
        embed.add_field(name="RAM Usage", value=f"{ram_usage_str}%")
        embed.add_field(
            name="Upload Speed", value=f"{upload_speed:.2f} MB/s ({bytes_sent} B)"
        )
        embed.add_field(
            name="Download Speed",
            value=f"{download_speed:.2f} MB/s ({bytes_received} B)",
        )

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Sys_info(bot))
