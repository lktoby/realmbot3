import typing
import discord
import discord.ext
from discord.ext import commands
import datetime


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # r!ping
    async def ping(self, ctx):
        ping = round(self.bot.latency, 2) * 1000
        await ctx.send(f'pong! {ping}ms')

    @commands.command()  # r!guide
    @commands.has_any_role(828588365674315777, 842174930778849313, 792531914887266364, 765646532149379072,
                           842174930405294130, 792531914119839754, 766994066260754433, 842174930405294130,
                           792531913797140540, 763126817179303959, 842174929936056342, 792531912584855582,
                           767064778916888596, 842174929670635550, 792116499308478496, 764525491880329216)
    async def guide(self, ctx):
        embed = discord.Embed(title="in case your forgot how i work",
                              description="`r!add am/pm/both <emoji> <name> <number>` adds a portal\n`r!delete/r!remove "
                                          "<#channel>` deletes a portal",
                              color=0xfdfd96)
        await ctx.send(embed=embed)

    @guide.error
    async def guide_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            ctx.send('this command isn\'t for you >:(')

    @commands.command()  # r!list
    async def list(self, ctx):
        embed = discord.Embed(title="commands available",
                              description="`r!help` - shows a brief description for realm bot\n`r!portals` - shows how many portals we have at the moment\n`r!userinfo` - shows "
                                          "information about a user\n`r!serverinfo` - shows information about this "
                                          "server\n`r!inviteinfo` - shows information about an invite\n`r!portals` - shows how many portals we have listed\nrun `r!help "
                                          "[name of command]` to see detailed usage of each command\narguments marked "
                                          "in <> are required arguments, while arguments marked in [] are optional "
                                          "arguments",
                              color=0xfdfd96)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.group(name='help', invoke_without_command=True)  # r!help
    async def help_group(self, ctx):
        embed = discord.Embed(title="you summoned me :o",
                              description="hi i'm realm bot, the bot that secretly powers this server realm of "
                                          "portals!\nyou can run `r!list` for a list of my commands available!\nyou "
                                          "can take a look at my source code at "
                                          "https://github.com/lktoby/realmbot3\nif you have any ideas for realm bot, "
                                          "feel free to suggest any ideas by running `??suggest <your suggestion>` in "
                                          "<#763141913272123453>!",
                              color=0xfdfd96, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="developed by toby#0508 ; version 0.0.5")
        await ctx.send(embed=embed)

    @help_group.command(name='list', aliases=['cmds', 'commands'])  # r!help list
    async def list_subcommand(self, ctx):
        embed = discord.Embed(title="commands", description="list out all the current commands i have",
                              color=0xfdfd96, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="aliases", value="cmds, commands", inline=False)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @help_group.command(name='userinfo', aliases=['whois', 'uinfo', 'ui'])  # r!help userinfo
    async def userinfo_subcommand(self, ctx):
        embed = discord.Embed(title="userinfo [@user/id]", description="shows information about a specified user",
                              color=0xfdfd96, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="aliases", value="whois, uinfo, ui", inline=False)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @help_group.command(name='inviteinfo', aliases=['check', 'inv', 'invite'])  # r!help inviteinfo
    async def inviteinfo_subcommand(self, ctx):
        embed = discord.Embed(title="inviteinfo <invite link>",
                              description="shows the information about the server fetched from an invite specified",
                              color=0xfdfd96, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="aliases", value="check, inv, invite", inline=False)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @help_group.command(name='serverinfo', aliases=['sinfo', 'server', 'info'])  # r!help serverinfo
    async def serverinfo_subcommand(self, ctx):
        embed = discord.Embed(title="serverinfo", description="shows the information about the server", color=0xfdfd96)
        embed.add_field(name="aliases", value="sinfo, server, info", inline=False)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @help_group.command(name='categoryinfo', aliases=['cinfo'])  # r!help categoryinfo
    async def categoryinfo_subcommand(self, ctx):
        embed = discord.Embed(title="categoryinfo <category>",
                              description="shows the information about the specified category", color=0xfdfd96)
        embed.add_field(name="aliases", value="cinfo", inline=False)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @help_group.command(name='portals', aliases=['count'])  # r!help guide
    async def portals_subcommand(self, ctx):
        embed = discord.Embed(title="portals <apm/head/realm1/realm2/nsfw/all>",
                              description="shows how many portals we have listed", color=0xfdfd96)
        embed.add_field(name="aliases", value="count", inline=False)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @help_group.command(name='query', aliases=['whoowns', 'owners'])
    async def query_subcommand(self, ctx):
        embed = discord.Embed(title="query <channel>/<@owner>",
                              description="shows the owners of the portal (if channel is input)\nshows the channel the person is listed as the owner of",
                              color=0xfdfd96)
        embed.add_field(name="aliases", value="whoowns, owners", inline=False)
        embed.set_footer(text=f"summoned by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    def calculatetime(self, age):  # calculate time and mention how long has it been in a human readable format
        hours, remainder = divmod(int(age.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        format = f'{days} days, {hours} hours, {minutes} minutes and {seconds} seconds'
        return format

    @commands.command(aliases=['whois', 'uinfo', 'ui'])  # r!userinfo
    async def userinfo(self, ctx, ping: typing.Optional[discord.Member]):
        if ping is None:
            member = ctx.message.author
        else:
            member = ping
        staffroles = []
        if ctx.guild.get_role(764525491880329216) in member.roles:  # owner
            staffroles.append(ctx.guild.get_role(764525491880329216).mention)
        elif ctx.guild.get_role(767064778916888596) in member.roles:  # pr manager
            staffroles.append(ctx.guild.get_role(767064778916888596).mention)
        if ctx.guild.get_role(763126817179303959) in member.roles:  # admin
            staffroles.append(ctx.guild.get_role(763126817179303959).mention)
        elif ctx.guild.get_role(766994066260754433) in member.roles:  # mod
            staffroles.append(ctx.guild.get_role(766994066260754433).mention)
        elif ctx.guild.get_role(818577794900033596) in member.roles:  # pr team
            staffroles.append(ctx.guild.get_role(818577794900033596).mention)
        elif ctx.guild.get_role(765646532149379072) in member.roles:  # helper
            staffroles.append(ctx.guild.get_role(765646532149379072).mention)
        elif ctx.guild.get_role(828747158920495154) in member.roles:  # 18+
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
        if ctx.guild.get_role(764842858179985408) in member.roles:  # ver apm
            linkedroles.append(ctx.guild.get_role(764842858179985408).mention)
        if ctx.guild.get_role(764842866446303232) in member.roles:  # exp apm
            linkedroles.append(ctx.guild.get_role(764842866446303232).mention)
        elif ctx.guild.get_role(764842642257084416) in member.roles:  # new apm
            linkedroles.append(ctx.guild.get_role(764842642257084416).mention)
        if ctx.guild.get_role(763463442333696011) in member.roles:  # linked apm
            linkedroles.append(ctx.guild.get_role(763463442333696011).mention)
        if ctx.guild.get_role(792519836893970462) in member.roles:  # linked2 apm
            linkedroles.append(ctx.guild.get_role(792519836893970462).mention)
        if ctx.guild.get_role(845321307805712415) in member.roles:  # verified head apm
            linkedroles.append(ctx.guild.get_role(845321307805712415).mention)
        if ctx.guild.get_role(846156350002298960) in member.roles:  # exp head apm
            linkedroles.append(ctx.guild.get_role(846156350002298960).mention)
        if ctx.guild.get_role(846156356548296795) in member.roles:  # linked head apm
            linkedroles.append(ctx.guild.get_role(846156356548296795).mention)
        if ctx.guild.get_role(765627008028901396) in member.roles:  # retired
            linkedroles.append(ctx.guild.get_role(765627008028901396).mention)
        if ctx.guild.get_role(790331133644242987) in member.roles:  # community
            linkedroles.append(ctx.guild.get_role(790331133644242987).mention)
        if len(linkedroles) < 1:
            linkedroles.append("none")

        embed.add_field(name="linked status", value=f'\n'.join(linkedroles))

        apmroles = []
        if ctx.guild.get_role(763463689025749033) in member.roles:  # pm
            apmroles.append(ctx.guild.get_role(763463689025749033).mention)
        if ctx.guild.get_role(763463659631804456) in member.roles:  # am
            apmroles.append(ctx.guild.get_role(763463659631804456).mention)
        if ctx.guild.get_role(846198680095948861) in member.roles:  # head pm
            apmroles.append(ctx.guild.get_role(846198680095948861).mention)
        if ctx.guild.get_role(846198683158708244) in member.roles:  # head am
            apmroles.append(ctx.guild.get_role(846198683158708244).mention)
        if len(apmroles) < 1:
            apmroles.append("none")

        embed.add_field(name="apm status", value=f'\n'.join(apmroles))
        embed.add_field(name="Created at",
                        value=f'{member.created_at.strftime("%d %b %Y")}; {self.calculatetime(memberage)} ago',
                        inline=True)
        embed.add_field(name="Joined at",
                        value=f'{member.joined_at.strftime("%d %b %Y")}; {self.calculatetime(serverage)} ago')
        embed.set_footer(text=f'user id: {member.id}')
        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.RoleNotFound):
            embed = discord.Embed(title="use this command in realm 1", color=0xff4747)
            embed.set_footer(text='because toby is too lazy to configure this command to be used in every realm server')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="user not found.", color=0xff4747)
        await ctx.send(embed=embed)
        print(f'userinfo command ran into an error: {error}')

    @commands.command(aliases=['check', 'inv', 'invite'])  # r!inviteinfo
    async def inviteinfo(self, ctx, invite):
        inv = await ctx.bot.fetch_invite(invite)
        print(f'{inv} is being queried to be checked')
        embed = discord.Embed(title=f"information fetched from {inv.code}", color=0xfdfd96)
        embed.set_thumbnail(url=f'{inv.guild.icon_url}')
        embed.add_field(name='server name', value=f'{inv.guild.name}')
        embed.add_field(name='server id', value=f'{inv.guild.id}', inline=False)
        embed.add_field(name='server created at', value=f'{inv.guild.created_at.strftime("%d %b %Y, %H:%M")}',
                        inline=False)
        embed.add_field(name='member count', value=f'{inv.approximate_member_count}', inline=False)
        embed.add_field(name='verification level', value=f'{str(inv.guild.verification_level)}', inline=False)
        if inv.max_age == 0:
            embed.add_field(name='invite expires in', value='never', inline=False)
            await ctx.send(embed=embed)
        else:
            expire = inv.max_age
            embed.add_field(name='invite expires in', value=f'{expire}', inline=False)
            await ctx.send(embed=embed)
        print(f'{inv} has been checked')

    @inviteinfo.error
    async def inviteinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="please input an invite.", color=0xff4747)
            await ctx.send(embed=embed)
        else:
            print(f'inviteinfo command ran into an error: {error}')
            embed = discord.Embed(title="invalid invite.", color=0xff4747)
            await ctx.send(embed=embed)

    @commands.command(aliases=['sinfo', 'server', 'info'])  # r!serverinfo
    async def serverinfo(self, ctx):
        server = ctx.guild
        serverage = datetime.datetime.now() - server.created_at
        humans = 0
        bots = 0
        txt = 0
        voice = 0
        category = 0
        for member in server.members:
            if member.bot:
                bots += 1
            else:
                humans += 1
        for channel in server.channels:
            if channel.type == discord.ChannelType.text or channel.type == discord.ChannelType.news:
                txt += 1
            elif channel.type == discord.ChannelType.voice or channel.type == discord.ChannelType.stage_voice:
                voice += 1
            elif channel.type == discord.ChannelType.category:
                category += 1
        embed = discord.Embed(title=f'info about {server.name}', color=0xfdfd96)
        embed.set_thumbnail(url=f'{server.icon_url}')
        embed.add_field(name=f'{server.member_count} members',
                        value=f'Bots: {bots}\nHumans: {humans}', inline=True)
        embed.add_field(name="Created at",
                        value=f'{server.created_at.strftime("%d %b %Y")}; {self.calculatetime(serverage)} ago',
                        inline=True)
        embed.add_field(name="Owner", value=f'{server.owner.name}#{server.owner.discriminator}, ID: {server.owner.id}',
                        inline=True)
        embed.add_field(name=f'{len(server.channels)} channels',
                        value=f'Text: {txt}\nVoice: {voice}\nCategories: {category}', inline=True)
        embed.add_field(name="Roles", value=f'{len(server.roles)}', inline=True)
        embed.add_field(name="Boosts",
                        value=f'Boost level: {server.premium_tier}\nBoosters: {server.premium_subscription_count}',
                        inline=True)
        embed.set_footer(text=f'Server ID: {server.id}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['cinfo'])
    async def categoryinfo(self, ctx, cat: discord.CategoryChannel):
        embed = discord.Embed(title=f'info for category {cat.name}', color=0xfdfd96)
        embed.add_field(name='id', value=f'{cat.id}', inline=False)
        embed.add_field(name='created at',
                        value=f'{cat.created_at.strftime("%d %b %Y")}; {self.calculatetime(datetime.datetime.now() - cat.created_at)} ago',
                        inline=False)
        if len(cat.text_channels) < 50:
            embed.add_field(name=f'{len(cat.text_channels)} text channels', value='category not full', inline=False)
        else:
            embed.add_field(name=f'{len(cat.text_channels)} text channels', value='category full', inline=False)
        await ctx.send(embed=embed)

    @categoryinfo.error
    async def categoryinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title='please input a category.', color=0xff4747)
            await ctx.send(embed=embed)
        else:
            print(f'command categoryinfo ran into an error: {error}')


def setup(bot):
    bot.add_cog(Info(bot))
