import typing
import discord
import discord.ext
from discord.ext import commands
import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency, 2) * 1000
        await ctx.send(f'pong! {ping}ms')

    @commands.command()
    @commands.has_any_role(828588365674315777, 842174930778849313, 792531914887266364, 765646532149379072, 842174930405294130, 792531914119839754, 766994066260754433, 842174930405294130, 792531913797140540, 763126817179303959, 842174929936056342, 792531912584855582, 767064778916888596, 842174929670635550, 792116499308478496, 764525491880329216)
    async def guide(self, ctx):
        embed = discord.Embed(title="in case your forgot how i work",
                              description="`r!add am/pm/both <emoji> <name> <number>` adds a portal\n`r!delete <#channel>` deletes a portal",
                              color=0xfdfd96)
        await ctx.send(embed=embed)

    @guide.error
    async def guide_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            ctx.send('this command isn\'t for you >:(')

    @commands.group(name='help')
    async def help(self, ctx):
        embed = discord.Embed(title="you summoned me :o",
                              description="hi i'm realm bot, the bot that secretly powers this server realm of portals!\nfor now i don't have any public commands yet, so please stay tuned for any updates!\nyou can take a look at my source code at https://github.com/lktoby/realmbot3\nif you have any ideas for realm bot, feel free to suggest any ideas by running `??suggest <your suggestion>` in <#763141913272123453>!",
                              color=0xfdfd96, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="developed by toby#0508 ; version 0.0.2")
        await ctx.send(embed=embed)

    @help.command(aliases=['whois', 'uinfo', 'ui'])
    async def userinfo_subcommand(self, ctx):
        embed = discord.Embed(title="userinfo [@user/id]", description="shows information about a specified user",
                              color=0xfdfd96, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f"summoned by {ctx.message.author}")
        await ctx.send(embed=embed)

    def calculatetime(self, age):  # calculate time and mention how long has it been in a human readable format
        hours, remainder = divmod(int(age.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        format = f'{days} days, {hours} hours, {minutes} minutes and {seconds} seconds'
        return format

    @commands.command(aliases=['whois', 'uinfo', 'ui'])
    async def userinfo(self, ctx, ping: typing.Optional[discord.Member]):
        if ping is None:
            member = ctx.message.author
        else:
            member = ping
        staffroles = []
        if ctx.guild.get_role(764525491880329216) in member.roles: # owner
            staffroles.append(ctx.guild.get_role(764525491880329216).mention)
        elif ctx.guild.get_role(767064778916888596) in member.roles: # pr manager
            staffroles.append(ctx.guild.get_role(767064778916888596).mention)
        if ctx.guild.get_role(763126817179303959) in member.roles: # admin
            staffroles.append(ctx.guild.get_role(763126817179303959).mention)
        elif ctx.guild.get_role(766994066260754433) in member.roles: # mod
            staffroles.append(ctx.guild.get_role(766994066260754433).mention)
        elif ctx.guild.get_role(818577794900033596) in member.roles: # pr team
            staffroles.append(ctx.guild.get_role(818577794900033596).mention)
        elif ctx.guild.get_role(765646532149379072) in member.roles: # helper
            staffroles.append(ctx.guild.get_role(765646532149379072).mention)
        elif ctx.guild.get_role(828747158920495154) in member.roles: # 18+
            staffroles.append(ctx.guild.get_role(828747158920495154).mention)
        if len(staffroles) < 1:
            staffroles.append("none")

        memberage = datetime.datetime.now() - member.created_at
        serverage = datetime.datetime.now() - member.joined_at
        embed = discord.Embed(color=0xfdfd96, title=f'**{len(member.roles)} roles**')
        embed.set_author(name=f'{member}', url=f'{member.avatar_url}')
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.add_field(name="staff roles", value=f'\n'.join(staffroles))

        booster = False
        if ctx.guild.premium_subscriber_role in member.roles:
            booster = True
        embed.add_field(name="booster status", value=str(booster))

        linkedroles = []
        if ctx.guild.get_role(764842858179985408) in member.roles: # ver apm
            linkedroles.append(ctx.guild.get_role(764842858179985408).mention)
        if ctx.guild.get_role(764842866446303232) in member.roles: # exp apm
            linkedroles.append(ctx.guild.get_role(764842866446303232).mention)
        elif ctx.guild.get_role(764842642257084416) in member.roles: # new apm
            linkedroles.append(ctx.guild.get_role(764842642257084416).mention)
        if ctx.guild.get_role(764842642257084416) in member.roles: # linked apm
            linkedroles.append(ctx.guild.get_role(763463442333696011).mention)
        if ctx.guild.get_role(792519836893970462) in member.roles: # linked2 apm
            linkedroles.append(ctx.guild.get_role(792519836893970462).mention)
        if ctx.guild.get_role(845321307805712415) in member.roles: # verified head apm
            linkedroles.append(ctx.guild.get_role(845321307805712415).mention)
        if ctx.guild.get_role(846156350002298960) in member.roles: # exp head apm
            linkedroles.append(ctx.guild.get_role(846156350002298960).mention)
        if ctx.guild.get_role(846156356548296795) in member.roles: # linked head apm
            linkedroles.append(ctx.guild.get_role(846156356548296795).mention)
        if ctx.guild.get_role(765627008028901396) in member.roles: # retired
            linkedroles.append(ctx.guild.get_role(765627008028901396).mention)
        if ctx.guild.get_role(790331133644242987) in member.roles: # community
            linkedroles.append(ctx.guild.get_role(790331133644242987).mention)
        if len(linkedroles) < 1:
            linkedroles.append("none")

        embed.add_field(name="linked status", value=f'\n'.join(linkedroles))

        apmroles = []
        if ctx.guild.get_role(763463689025749033) in member.roles: # pm
            apmroles.append(ctx.guild.get_role(763463689025749033).mention)
        if ctx.guild.get_role(763463659631804456) in member.roles: # am
            apmroles.append(ctx.guild.get_role(763463659631804456).mention)
        if ctx.guild.get_role(846198680095948861) in member.roles: # head pm
            apmroles.append(ctx.guild.get_role(846198680095948861).mention)
        if ctx.guild.get_role(846198683158708244) in member.roles: # head am
            apmroles.append(ctx.guild.get_role(846198683158708244).mention)
        if len(linkedroles) < 1:
            linkedroles.append("none")

        embed.add_field(name="apm status", value=f'\n'.join(apmroles))
        embed.add_field(name="Created at",
                        value=f'{member.created_at.strftime("%d %b %Y")}; {self.calculatetime(memberage)} ago',
                        inline=True)
        embed.add_field(name="Joined at",
                        value=f'{member.joined_at.strftime("%d %b %Y")}; {self.calculatetime(serverage)} ago')
        embed.set_footer(text=f'Username: {member.name}, user id: {member.id}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))