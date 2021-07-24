import discord
from discord.ext import commands
from dog import Client
import os
import requests
from random import *


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # roast
    @commands.command(name='roast')
    async def roast(self, ctx, target: discord.Member, *, msg):
        roastable = [ctx.guild.get_member(477096301364903936), ctx.guild.get_member(750822039438491669), ctx.guild.get_member(553401127731855364), ctx.guild.get_member(449057790963613716), ctx.guild.get_member(320245258250223618), ctx.guild.get_member(479113259753013258), ctx.guild.get_member(709959792537632810), ctx.guild.get_member(472893119990595594), ctx.guild.get_member(326448696042586112)]
        if target not in roastable:
            embed=discord.Embed(title='this member isn\'t roastable!', color=0xff4747)
            await ctx.send(embed=embed)
            return
        author = ctx.message.author
        embed = discord.Embed(title=f'a roast from {author.name} to {target.name}!', description=msg, color=0xfdfd96)
        embed.set_footer(icon_url=author.avatar_url, text='submit a new roast by running r!roast <target> <message>')
        embed.set_thumbnail(url=target.avatar_url)
        channel = ctx.guild.get_channel(778676762808549406)
        await channel.send(content=f'{target.mention} you just got a new incoming roast!', embed=embed)
        embed = discord.Embed(title='roast sent!', color=0xfdfd96)
        await ctx.send(embed=embed)

    @roast.error
    async def roast_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f'did you miss something?', description='remember the format is `r!roast <target> <message>`.', color=0xff4747)
            await ctx.send(embed=embed)
        print(f'roast command ran into an error: {error}')

    # dog pics (thedogapi)
    @commands.command(name='dog')
    async def dog (self, ctx):
        dog = Client(os.getenv('DOG_API_KEY'))
        image = dog.get_images()[0]
        embed = discord.Embed(title=f'{ctx.message.author.name} just found a dog!', color=0xfdfd96)
        embed.set_image(url=image.url)
        await ctx.send(embed=embed)

    # cat pics (thecatapi)
    @commands.command(name='cat')
    async def cat(self, ctx):
        r = requests.get("https://api.thecatapi.com/v1/images/search").json()
        embed=discord.Embed(title=f'{ctx.message.author.name} just found a cat!', color=0xfdfd96)
        embed.set_image(url=r[0]['url'])
        await ctx.send(embed=embed)

    # random aes generator
    @commands.command(name='aesthetic', aliases=['aes'])
    async def aesthetic(self, ctx):
        aes = ['angelcore', 'cottagecore', 'cyberpunk', 'fairycore', 'grunge', 'draincore', 'mangacore', 'soft grunge', 'dollcore', 'webcore', 'medcore/hospital', 'babycore', 'steampunk', 'dark academia', 'light academia', 'indie', '90s', 'pastel', 'kidcore', 'retro', 'vaporwave', 'sleepycore', 'lovecore', 'devilcore', 'royalcore', 'princesscore', 'bunnycore', 'bloomcore', 'beachcore', 'urbancore', 'citycore', 'y2k', 'animecore', 'cartooncore', 'messycore', 'cybercore', 'cafe', 'emo', 'glitchcore', 'traumacore']
        pos = randint(1, len(aes))
        result = aes[pos]
        embed = discord.Embed(title=f'generated aesthetic: {result}', color=0xfdfd96)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))