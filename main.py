import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sys
import traceback

intents = discord.Intents.all()
intents.members = True

game = discord.Activity(name="i'm back from the dead", type=discord.ActivityType.playing)
bot = commands.Bot(command_prefix=commands.when_mentioned_or('r!'), intents=intents, activity=game)
bot.remove_command('help')


load_dotenv()
TOKEN = os.getenv('TOKEN')


@bot.event
async def on_ready():
    print('---------------------')
    print(f'logged in as {bot.user.name}')
    print('---------------------')

initial_extensions = ['cogs.info', 'cogs.portals', 'cogs,apply']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run(TOKEN)
