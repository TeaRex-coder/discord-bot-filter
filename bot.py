import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

if DISCORD_TOKEN is None or GUILD_ID is None:
    raise RuntimeError("DISCORD_TOKEN or GUILD_ID not found in .env")

try:
    GUILD_ID = int(GUILD_ID)
except ValueError:
    raise RuntimeError("GUILD_ID must be an integer")

# intents to read user data
intents = discord.Intents.default()
intents.members = True

# create bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)

# register bot
from commands.botsCommand import register as register_bots_command

register_bots_command(bot, GUILD_ID)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
