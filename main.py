import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

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

bot.load_extension('cogs.portals')

'''
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="command does not exist.", color=0xffb6c1)
        await ctx.send(embed=embed)
        '''

bot.run(TOKEN)
