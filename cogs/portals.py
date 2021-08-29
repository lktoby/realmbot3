import inspect
import logging

import discord
from discord.ext import commands

log = logging.getLogger(__name__)

pcount = 0
hcount = 0


class Portals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="add")
    @commands.has_permissions(manage_channels=True)
    async def add(self, ctx: commands.Context):
        global pcount

    @add.command(name="pm")
    async def pm_subcommand(self, ctx: commands.Context, emoji, pname, num):
        global pcount, hcount
        if ctx.guild.id == 763124398046969897:  # realm 1
            category = ctx.guild.get_channel(778633618691850250)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 792101190154453043:  # realm 2
            category = ctx.guild.get_channel(864572866153807944)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 860255811732111391:  # realm 3
            category = ctx.guild.get_channel(861742133231747092)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 840406812423094272:  # head realm
            category = ctx.guild.get_channel(843544254579474513)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            hcount += 1

    @add.command(name="am")
    async def am_subcommand(self, ctx, emoji, pname, num):
        global pcount, hcount
        if ctx.guild.id == 763124398046969897:  # realm 1
            category = ctx.guild.get_channel(812098840802623488)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 792101190154453043:  # realm 2
            category = ctx.guild.get_channel(854742936368316446)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 860255811732111391:  # realm 3
            category = ctx.guild.get_channel(860258321985306725)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 840406812423094272:  # head realm
            category = ctx.guild.get_channel(843544276691320863)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            hcount += 1

    @add.command(name="both")
    async def both_subcommand(self, ctx: commands.Context, emoji, pname, num):
        global pcount, hcount
        if ctx.guild.id == 763124398046969897:  # realm 1
            category = ctx.guild.get_channel(773916338002722817)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 792101190154453043:  # realm 2
            category = ctx.guild.get_channel(827224133279809576)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 860255811732111391:  # realm 3
            category = ctx.guild.get_channel(861742253134577684)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild.id == 840406812423094272:  # head realm
            category = ctx.guild.get_channel(860269639664664597)
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}", category=category
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new channel {channel.id} has been created.")
            hcount += 1

    @add.command(name="nsfw")
    @commands.has_role(828588365674315777)
    async def nsfw_subcommand(
        self, ctx: commands.Context, emoji, pname, num
    ):  # r!add nsfw emoji name number
        global pcount, hcount
        if ctx.guild == 792101190154453043:
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}",
                category=ctx.guild.get_channel(827505074401050634),
                nsfw=True,
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new nsfw channel {channel.id} has been created.")
            pcount += 1
        elif ctx.guild == 840406812423094272:
            channel = await ctx.guild.create_text_channel(
                name=f"{emoji}・{pname}・{num}",
                category=ctx.guild.get_channel(845489191710097458),
                nsfw=True,
            )
            await ctx.send(f"{channel.mention} has been created.")
            log.info(f"new nsfw channel {channel.id} has been created.")
            hcount += 1

    @add.error
    async def add_error(self, ctx: commands.Context, error, param):
        param = inspect.Parameter
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=f"did you forget {param}?", color=0xFF4747)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="this command isn't for you noob", color=0xFF4747
            )
            await ctx.send(embed=embed)

    @commands.command(name="delete", aliases=["remove", "rm", "del"])
    @commands.has_permissions(manage_channels=True)
    async def delete(
        self, ctx: commands.Context, channel: discord.TextChannel
    ):  # r! delete channel
        if ctx.guild == 763124398046969897 or 792101190154453043:
            global pcount
            await channel.delete()
            await ctx.send("channel successfully deleted.")
            pcount -= 1
        elif ctx.guild == 840406812423094272:
            global hcount
            await channel.delete()
            await ctx.send("channel successfully deleted.")

    @delete.error
    async def delete_error(self, ctx: commands.Context, error):
        if isinstance(error, discord.NotFound):
            embed = discord.Embed(title="channel does not exist!", color=0xFF4747)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("this command isn't for you >:(")

    @commands.command(name="count", aliases=["portals"])
    async def count(self, ctx: commands.Context):  # r!count
        global pcount
        embed = discord.Embed(
            title=f"we currently have {pcount} portals listed.", color=0xFF4747
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Portals(bot))
