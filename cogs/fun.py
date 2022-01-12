import logging
import random

import aiohttp
import discord
from discord.ext import commands

log = logging.getLogger(__name__)


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        if self.session:
            self.bot.loop.create_task(self.session.close())

    # roast
    '''
    @commands.command(name="roast")
    async def roast(self, ctx: commands.Context, target: discord.Member, *, msg: str):
        roastable = [
            477096301364903936,
            750822039438491669,
            553401127731855364,
            449057790963613716,
            320245258250223618,
            479113259753013258,
            709959792537632810,
            472893119990595594,
            326448696042586112,
        ]
        if target.id not in roastable:
            embed = discord.Embed(title="this member isn't roastable!", color=0xFF4747)
            await ctx.send(embed=embed)
            return
        author = ctx.message.author
        embed = discord.Embed(
            title=f"a roast from {author.name} to {target.name}!",
            description=msg,
            color=0xFDFD96,
        )
        embed.set_footer(
            icon_url=author.avatar_url,
            text="submit a new roast by running r!roast <target> <message>",
        )
        embed.set_thumbnail(url=target.avatar_url)
        channel = ctx.guild.get_channel(778676762808549406)
        await channel.send(
            content=f"{target.mention} you just got a new incoming roast!", embed=embed
        )
        embed = discord.Embed(title="roast sent!", color=0xFDFD96)
        await ctx.send(embed=embed)

    @roast.error
    async def roast_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title=f"did you miss something?",
                description="remember the format is `r!roast <target> <message>`.",
                color=0xFF4747,
            )
            await ctx.send(embed=embed)
        log.error(f"roast command ran into an error: {error}")
        '''

    # dog pics (thedogapi)
    @commands.command()
    async def dog(self, ctx: commands.Context):
        async with self.session.get("https://api.thedogapi.com/v1/images/search") as res:
            if res.status != 200:
                return await ctx.send("something went wrong, try again!")
            r = await res.json()
        embed = discord.Embed(title=f"{ctx.message.author.name} just found a dog!", color=0xFDFD96)
        embed.set_image(url=r[0]["url"])
        await ctx.send(embed=embed)

    # cat pics (thecatapi)
    @commands.command()
    async def cat(self, ctx: commands.Context):
        async with self.session.get("https://api.thecatapi.com/v1/images/search") as res:
            if res.status != 200:
                return await ctx.send("something went wrong, try again!")
            r = await res.json()
        embed = discord.Embed(title=f"{ctx.message.author.name} just found a cat!", color=0xFDFD96)
        embed.set_image(url=r[0]["url"])
        await ctx.send(embed=embed)

    # random aes generator
    @commands.command(aliases=["aes"])
    async def aesthetic(self, ctx: commands.Context):
        aes = [
            "angelcore",
            "cottagecore",
            "cyberpunk",
            "fairycore",
            "grunge",
            "draincore",
            "mangacore",
            "soft grunge",
            "dollcore",
            "webcore",
            "medcore/hospital",
            "babycore",
            "steampunk",
            "dark academia",
            "light academia",
            "indie",
            "90s",
            "pastel",
            "kidcore",
            "retro",
            "vaporwave",
            "sleepycore",
            "lovecore",
            "devilcore",
            "royalcore",
            "princesscore",
            "bunnycore",
            "bloomcore",
            "beachcore",
            "urbancore",
            "citycore",
            "y2k",
            "animecore",
            "cartooncore",
            "messycore",
            "cybercore",
            "cafe",
            "emo",
            "glitchcore",
            "traumacore",
        ]
        pos = random.randint(1, len(aes))
        result = aes[pos]
        embed = discord.Embed(title=f"generated aesthetic: {result}", color=0xFDFD96)
        await ctx.send(embed=embed)

    # random colour generator
    @commands.command(name="colour", aliases=["color"])
    async def colour(self, ctx: commands.Context):
        randhex = discord.Colour.random()
        log.info(randhex)
        async with self.session.get(
            f"https://singlecolorimage.com/get/{str(randhex)[1:]}/512x512.png"
        ) as res:
            if res.status != 200:
                return await ctx.send("something went wrong, try again!")
            image = str(res.url)
        embed = discord.Embed(title=f"generated colour hex: {str(randhex)}", color=randhex)
        embed.set_thumbnail(url=image)
        await ctx.send(embed=embed)

    # codeblock command
    @commands.command(name="codeblock", aliases=['cb'])
    async def codeblock(self, ctx: commands.Context, *, content):
        await ctx.send(f"```{content}```")

    @codeblock.error
    async def codeblock_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="insert something to be put in codeblock", color=0xff4747)
            await ctx.send(embed=embed)
        print(error)


def setup(bot):
    bot.add_cog(Fun(bot))
