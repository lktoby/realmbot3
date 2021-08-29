import logging
import os
import sys
import traceback

import discord
import rich
from discord.ext import commands
from dotenv import load_dotenv

log = logging.getLogger(__name__)

game = discord.Activity(name="i'm back from the dead", type=discord.ActivityType.playing)
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("r!"), intents=discord.Intents.all(), activity=game
)
bot.remove_command("help")


load_dotenv()
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print_msg = [
        f"logged in as {bot.user.name}",
        f"i am developed by toby#0508 ",
        f"Prefix: r!",
        "Connected to:",
        f"{len(bot.guilds)} servers",
        f"Invite URL: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot+applications.commands&permissions=0",
    ]
    WIDTH = len(max(print_msg, key=len))
    print_msg = [s.center(WIDTH) for s in print_msg]
    [print_msg.insert(index, "-" * WIDTH) for index in (0, 2, len(print_msg) + 2)]
    rich.print("\n".join(print_msg))


initial_extensions = ["cogs.info", "cogs.portals", "cogs.noms", "cogs.fun"]

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            log.error(f"Failed to load extension {extension}.", file=sys.stderr)
            traceback.print_exc()

bot.run(TOKEN)
