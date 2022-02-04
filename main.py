import logging
import os
import sys
import traceback
from datetime import datetime

import discord
import rich
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand

log = logging.getLogger(__name__)

# Logs to ./logs folder on every boot

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"logs/{dt_string}.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


game = discord.Activity(name="dm postals not toby", type=discord.ActivityType.playing)
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("r!"), intents=discord.Intents.all(), activity=game
)
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)

load_dotenv()
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print_msg = [
        f"logged in as {bot.user.name}",
        f"i am developed by toby#0508 ",
        f"Prefix: r!"
    ]
    WIDTH = len(max(print_msg, key=len))
    print_msg = [s.center(WIDTH) for s in print_msg]
    [print_msg.insert(index, "-" * WIDTH) for index in (0, 2, len(print_msg) + 2)]
    rich.print("\n".join(print_msg))


initial_extensions = ["cogs.info", "cogs.portals", "cogs.fun", "cogs.welc", "cogs.verification"]

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            log.error(f"Failed to load extension {extension}.", file=sys.stderr)
            traceback.print_exc()

bot.run(TOKEN)
