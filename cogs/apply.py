import os
import discord
from discord.ext import commands
import asyncio
from typing import Union
import datetime
from pbwrap import Pastebin


class Apply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    pb_api_key = os.environ['PB_API_KEY']
    pb_username = os.environ['PB_USERNAME']
    pb_pw = os.environ['PB_PASSWORD']

    pbapi = Pastebin(pb_api_key)
    print(f'api key for pastebin is {pbapi}')
    pbapi.authenticate(pb_username, pb_pw)

    global isopen

    @commands.group(name='status', aliases=['isopen'])
    async def status_group(self, ctx):
        global isopen
        if isopen:
            embed = discord.Embed(title="staff applications are open!",
                                  description="dm me `r!apply` if you have **level 5** on amari!\nrun `>r` to see if "
                                              "you fit the requirements",
                                  color=0xfdfdbe)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="staff applications are closed!",
                                  description="please check our <#763464426602364969> channel to see if we are in "
                                              "need of new staff!\nyou can also grab the <@&765641353630711829> ping "
                                              "to be updated with us!",
                                  color=0xfdfdbe)
            await ctx.send(embed=embed)

    @status_group.command(name='toggle')
    @commands.is_owner()
    async def toggle_subcommand(self, ctx, value):
        global isopen
        if value == "true":
            isopen = True
            await ctx.send('application status has been set to: **true**.')
        elif value == "false":
            isopen = False
            await ctx.send('application status has been set to: **false**.')
        else:
            await ctx.send('toby remember the values are "true" and "false"')

    @commands.dm_only()
    @commands.has_role(778947452719726603)
    async def apply(self, ctx):
        global isopen
        if not isopen:
            ctx.command.update(enabled=False)
            return
        response = {
            "applicant": f"{ctx.message.author.name}#{ctx.message.author.discriminator}, id: {ctx.message.author.id}",
            "submission time": datetime.datetime.utcnow()
        }
        embed = discord.Embed(title="welcome to the realm of portals helper application!",
                              description="please take around 15-20 minutes to finish this application. \nbe truthful "
                                          "and be confident in your answers. \neach answer has a timeout of 15 "
                                          "minutes. good luck :D",
                              color=0xfdfdbe)
        embed.set_footer(text="please send anything to proceed to the application.")
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.channel

        try:
            await self.bot.wait_for(event='message', check=check, timeout=900)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="your response has timed out!",
                                  description="please run `r!apply` again to restart the application process.",
                                  color=0xff4747)
            await ctx.send(embed=embed)
        # how should we call you?
        else:
            embed = discord.Embed(title="how should we call you?", color=0xfdfdbe)
            embed.set_footer(text="e.g. toby")
            await ctx.send(embed=embed)
            try:
                response["name"] = await self.bot.wait_for(event='message', check=check, timeout=900)
            except asyncio.TimeoutError:
                embed = discord.Embed(title="your response has timed out!",
                                      description="please run `r!apply` again to restart the application process.",
                                      color=0xff4747)
                await ctx.send(embed=embed)
                return
            # what are your pronouns?
            else:
                embed = discord.Embed(title="what are your pronouns?", color=0xfdfdbe)
                embed.set_footer(text="e.g. she/her")
                await ctx.send(embed=embed)
                try:
                    response["pronouns"] = await self.bot.wait_for(event='message', check=check, timeout=900)
                except asyncio.TimeoutError:
                    embed = discord.Embed(title="your response has timed out!",
                                          description="please run `r!apply` again to restart the application process.",
                                          color=0xff4747)
                    await ctx.send(embed=embed)
                    return
                # what is your timezone?
                else:
                    embed = discord.Embed(title="what is your timezone?",
                                          description="please convert your timezone (e.g. CST) to GMT/UTC format ("
                                                      "e.g. GMT+8), use [this timezone converter]("
                                                      "https://greenwichmeantime.com/time-gadgets/time-zone-converter/) if you don't know how to convert",
                                          color=0xfdfdbe)
                    embed.set_footer(text="e.g. gmt+8")
                    await ctx.send(embed=embed)
                    try:
                        response["timezone"] = await self.bot.wait_for(event='message', check=check, timeout=900)
                    except asyncio.TimeoutError:
                        embed = discord.Embed(title="your response has timed out!",
                                              description="please run `r!apply` again to restart the application "
                                                          "process.",
                                              color=0xff4747)
                        await ctx.send(embed=embed)
                        return
                    # do you have 2fa turned on?
                    else:
                        embed = discord.Embed(title="do you have 2fa turned on?",
                                              description="react with :white_check:mark: if yes, :x: if no",
                                              color=0xfdfdbe)
                        await ctx.send(embed=embed)

                        def rcheck(r: discord.Reaction, u: Union[discord.Member, discord.User]):
                            return u.id == ctx.author.id and r.message.channel == ctx.channel and str(r.emoji) in [
                                "\U00002705", "\U0000274c"]

                        try:
                            reaction, user = await self.bot.wait_for(event='reaction_add', check=rcheck,
                                                                     timeout=900)
                        except asyncio.TimeoutError:
                            embed = discord.Embed(title="your response has timed out!",
                                                  description="please run `r!apply` again to restart the application "
                                                              "process.",
                                                  color=0xff4747)
                            await ctx.send(embed=embed)
                            return
                        else:
                            if str(reaction.emoji) == "\U00002705":
                                response["2fa"] = True
                            elif str(reaction.emoji) == "\U0000274c":
                                response["2fa"] = False
                            # why do you want to be a helper in realm of portals?
                            embed = discord.Embed(title="why do you want to be a helper in realm of portals?",
                                                  color=0xfdfdbe)
                            await ctx.send(embed=embed)
                            try:
                                response["1. why do you want to be a helper?"] = await self.bot.wait_for(
                                    event='message', check=check, timeout=900)
                            except asyncio.TimeoutError:
                                embed = discord.Embed(title="your response has timed out!",
                                                      description="please run `r!apply` again to restart the "
                                                                  "application process.",
                                                      color=0xff4747)
                                await ctx.send(embed=embed)
                                return
                            # what makes you a good fit to our team?
                            else:
                                embed = discord.Embed(title="what makes you a good fit to our team?",
                                                      color=0xfdfdbe)
                                await ctx.send(embed=embed)
                                try:
                                    response["2. what makes you a good fit?"] = await self.bot.wait_for(
                                        event='message', check=check, timeout=900)
                                except asyncio.TimeoutError:
                                    embed = discord.Embed(title="your response has timed out!",
                                                          description="please run `r!apply` again to restart the "
                                                                      "application process.",
                                                          color=0xff4747)
                                    await ctx.send(embed=embed)
                                    return
                                # how many hours do you spend on discord daily?
                                else:
                                    embed = discord.Embed(title="how many hours do you spend on discord daily?",
                                                          color=0xfdfdbe)
                                    await ctx.send(embed=embed)
                                    try:
                                        response[
                                            "3. how many hours do you spend on discord?"] = await self.bot.wait_for(
                                            event='message', check=check, timeout=900)
                                    except asyncio.TimeoutError:
                                        embed = discord.Embed(title="your response has timed out!",
                                                              description="please run `r!apply` again to restart the "
                                                                          "application process.",
                                                              color=0xff4747)
                                        await ctx.send(embed=embed)
                                        return
                                    # what do you usually use this server for?
                                    else:
                                        embed = discord.Embed(title="what do you usually use this server for?",
                                                              color=0xfdfdbe)
                                        await ctx.send(embed=embed)
                                        try:
                                            response[
                                                "4. what do you use this server for?"] = await self.bot.wait_for(
                                                event='message', check=check, timeout=900)
                                        except asyncio.TimeoutError:
                                            embed = discord.Embed(title="your response has timed out!",
                                                                  description="please run `r!apply` again to restart "
                                                                              "the application process.",
                                                                  color=0xff4747)
                                            await ctx.send(embed=embed)
                                            return
                                        # do you think your emotions can affect your performance as a helper?
                                        else:
                                            embed = discord.Embed(
                                                title="do you think your emotions can affect your performance as a "
                                                      "helper?",
                                                description="please answer on a scale of 1-5, where 1 is extremely "
                                                            "unlikely and 5 is extremely likely",
                                                color=0xfdfdbe)
                                        await ctx.send(embed=embed)
                                        try:
                                            response[
                                                "5. do you think your emotions can affect your performance?"] = await self.bot.wait_for(
                                                event='message', check=check, timeout=900)
                                        except asyncio.TimeoutError:
                                            embed = discord.Embed(title="your response has timed out!",
                                                                  description="please run `r!apply` again to restart "
                                                                              "the application process.",
                                                                  color=0xff4747)
                                            await ctx.send(embed=embed)
                                            return
                                        # annoying dms
                                        else:
                                            embed = discord.Embed(
                                                title="someone dms you about stuff happened in the server when you "
                                                      "were afk, they kept spamming you to a point where you find "
                                                      "them annoying, what do you do?",
                                                color=0xfdfdbe)
                                            await ctx.send(embed=embed)
                                            try:
                                                response[
                                                    "6. how do you deal with annoying dms?"] = await self.bot.wait_for(
                                                    event='message', check=check, timeout=900)
                                            except asyncio.TimeoutError:
                                                embed = discord.Embed(title="your response has timed out!",
                                                                      description="please run `r!apply` again to "
                                                                                  "restart the application process.",
                                                                      color=0xff4747)
                                                await ctx.send(embed=embed)
                                                return
                                            # fights
                                            else:
                                                embed = discord.Embed(
                                                    title="how do you deal with fights happening between members in our chats??",
                                                    color=0xfdfdbe)
                                                await ctx.send(embed=embed)
                                                try:
                                                    response[
                                                        "7. how do you deal with fights?"] = await self.bot.wait_for(
                                                        event='message', check=check, timeout=900)
                                                except asyncio.TimeoutError:
                                                    embed = discord.Embed(title="your response has timed out!",
                                                                          description="please run `r!apply` again to "
                                                                                      "restart the application "
                                                                                      "process.",
                                                                          color=0xff4747)
                                                    await ctx.send(embed=embed)
                                                    return
                                                # show your authority
                                                else:
                                                    embed = discord.Embed(
                                                        title="how do you show others that you are a staff member "
                                                              "that people have to listen to you/take your words "
                                                              "seriously? (except for changing your nickname)",
                                                        description="e.g. speak in a more affirmative manner, take "
                                                                    "action to pings faster",
                                                        color=0xfdfdbe)
                                                    await ctx.send(embed=embed)
                                                    try:
                                                        response[
                                                            "8. how do you show others that you are a staff member " \
                                                            "that people have to listen to you?"] = await \
                                                            self.bot.wait_for(
                                                            event='message', check=check, timeout=900)
                                                    except asyncio.TimeoutError:
                                                        embed = discord.Embed(title="your response has timed out!",
                                                                              description="please run `r!apply` again "
                                                                                          "to restart the application"
                                                                                          " process.",
                                                                              color=0xff4747)
                                                        await ctx.send(embed=embed)
                                                        return
                                                    # do you work for other apm hubs?
                                                    else:
                                                        embed = discord.Embed(
                                                            title="do you work for other apm hubs? please briefly "
                                                                  "describe where and what you do if any.",
                                                            description="p.s. this does not necessarily affect your "
                                                                        "chances of being picked, we just want to get "
                                                                        "to know about you more and make sure you "
                                                                        "won't feel overworked if you were chosen as "
                                                                        "a helper for realm.",
                                                            color=0xfdfdbe)
                                                        await ctx.send(embed=embed)
                                                        try:
                                                            response[
                                                                "9. do you work for other apm hubs?"] = await self.bot.wait_for(
                                                                event='message', check=check, timeout=900)
                                                        except asyncio.TimeoutError:
                                                            embed = discord.Embed(
                                                                title="your response has timed out!",
                                                                description="please run `r!apply` again to restart "
                                                                            "the application process.",
                                                                color=0xff4747)
                                                            await ctx.send(embed=embed)
                                                            return
                                                        # add request 1
                                                        else:
                                                            embed = discord.Embed(
                                                                title="please state if there is anything wrong with "
                                                                      "this request and how you would ask the person "
                                                                      "to change",
                                                                color=0xfdfdbe)
                                                            embed.set_image(
                                                                url="https://i.gyazo.com/4b18e1d7161fe43992a5e0f4b95e0ab0.png")
                                                            await ctx.send(embed=embed)
                                                            try:
                                                                response["add request 1"] = await self.bot.wait_for(
                                                                    event='message', check=check, timeout=900)
                                                            except asyncio.TimeoutError:
                                                                embed = discord.Embed(
                                                                    title="your response has timed out!",
                                                                    description="please run `r!apply` again to "
                                                                                "restart the application process.",
                                                                    color=0xff4747)
                                                                await ctx.send(embed=embed)
                                                                return
                                                            # add request 2
                                                            else:
                                                                embed = discord.Embed(
                                                                    title="please state if there is anything wrong "
                                                                          "with this request and how you would ask "
                                                                          "the person to change",
                                                                    color=0xfdfdbe)
                                                                embed.set_image(
                                                                    url="https://i.gyazo.com/369b7649f44382efbf08929869a498e1.png")
                                                                await ctx.send(embed=embed)
                                                                try:
                                                                    response[
                                                                        "add request 2"] = await self.bot.wait_for(
                                                                        event='message', check=check, timeout=900)
                                                                except asyncio.TimeoutError:
                                                                    embed = discord.Embed(
                                                                        title="your response has timed out!",
                                                                        description="please run `r!apply` again to "
                                                                                    "restart the application process.",
                                                                        color=0xff4747)
                                                                    await ctx.send(embed=embed)
                                                                    return
                                                                # add request 3
                                                                else:
                                                                    embed = discord.Embed(
                                                                        title="please state if there is anything "
                                                                              "wrong with this request and how you "
                                                                              "would ask the person to change",
                                                                        color=0xfdfdbe)
                                                                    embed.set_image(
                                                                        url="https://i.gyazo.com/e29b955a313f8b184bb38229cdaa4a74.png")
                                                                    await ctx.send(embed=embed)
                                                                try:
                                                                    response[
                                                                        "add request 3"] = await self.bot.wait_for(
                                                                        event='message', check=check, timeout=900)
                                                                except asyncio.TimeoutError:
                                                                    embed = discord.Embed(
                                                                        title="your response has timed out!",
                                                                        description="please run `r!apply` again to "
                                                                                    "restart the application process.",
                                                                        color=0xff4747)
                                                                    await ctx.send(embed=embed)
                                                                    return
                                                                # add request 4
                                                                else:
                                                                    embed = discord.Embed(
                                                                        title="please state if there is anything "
                                                                              "wrong with this request and how you "
                                                                              "would ask the person to change",
                                                                        color=0xfdfdbe)
                                                                    embed.set_image(
                                                                        url="https://i.gyazo.com/6135ff0dcccea5050fe51360e54ca172.png")
                                                                    await ctx.send(embed=embed)
                                                                try:
                                                                    response[
                                                                        "add request 4"] = await self.bot.wait_for(
                                                                        event='message', check=check, timeout=900)
                                                                except asyncio.TimeoutError:
                                                                    embed = discord.Embed(
                                                                        title="your response has timed out!",
                                                                        description="please run `r!apply` again to "
                                                                                    "restart the application process.",
                                                                        color=0xff4747)
                                                                    await ctx.send(embed=embed)
                                                                    return
                                                                # add request 5
                                                                else:
                                                                    embed = discord.Embed(
                                                                        title="please state if there is anything "
                                                                              "wrong with this request and how you "
                                                                              "would ask the person to change",
                                                                        color=0xfdfdbe)
                                                                    embed.set_image(
                                                                        url="https://i.gyazo.com/d236b642b27d91e1043c4bd570893f15.png")
                                                                    await ctx.send(embed=embed)
                                                                try:
                                                                    response[
                                                                        "add request 5"] = await self.bot.wait_for(
                                                                        event='message', check=check, timeout=900)
                                                                except asyncio.TimeoutError:
                                                                    embed = discord.Embed(
                                                                        title="your response has timed out!",
                                                                        description="please run `r!apply` again to "
                                                                                    "restart the application process.",
                                                                        color=0xff4747)
                                                                    await ctx.send(embed=embed)
                                                                    return
                                                                # final confirmation
                                                                else:
                                                                    embed = discord.Embed(
                                                                        title="finally, please be aware that:",
                                                                        description="1. what happens in staff chat "
                                                                                    "stays in staff chat\n2. do not "
                                                                                    "ask for perms that you are not "
                                                                                    "supposed to have\n3. you should "
                                                                                    "always be respectful to other "
                                                                                    "staff team members",
                                                                        color=0xfdfdbe)
                                                                    embed.set_footer(
                                                                        text="please react with the 🆗 emoji to continue")
                                                                    await ctx.send(embed=embed)

                                                                def rcheck2(r: discord.Reaction,
                                                                            u: Union[discord.Member, discord.User]):
                                                                    return u.id == ctx.author.id and r.message.channel == ctx.channel and str(
                                                                        r.emoji) in ["\U0001F197"]

                                                                try:
                                                                    reaction, user = await self.bot.wait_for(
                                                                        event='reaction_add', check=rcheck2,
                                                                        timeout=900)
                                                                except asyncio.TimeoutError:
                                                                    embed = discord.Embed(
                                                                        title="your response has timed out!",
                                                                        description="please run `r!apply` again to "
                                                                                    "restart the application process.",
                                                                        color=0xff4747)
                                                                    await ctx.send(embed=embed)
                                                                    return
                                                                # pr team preference
                                                                else:
                                                                    if str(reaction.emoji) == "\U0001F197":
                                                                        embed = discord.Embed(
                                                                        title="are you interested in being a part of "
                                                                              "the PR team?",
                                                                        description="the pr team mostly help with "
                                                                                    "modmail tickets, which includes "
                                                                                    "but not limited to: user/server "
                                                                                    "reports, blacklist requests, "
                                                                                    "ban appeals, "
                                                                                    "customer service.\n\nreact with "
                                                                                    ":white_check:mark: if yes, "
                                                                                    ":x: if no",
                                                                        color=0xfdfdbe)
                                                                        embed.set_footer(text="suge may have an "
                                                                                              "interview with you if "
                                                                                              "you say yes to this "
                                                                                              "option so please keep "
                                                                                              "your dms open")
                                                                        await ctx.send(embed=embed)
                                                                    try:
                                                                        reaction, user = await self.bot.wait_for(
                                                                            event='reaction_add', check=rcheck,
                                                                            timeout=900)
                                                                    except asyncio.TimeoutError:
                                                                        embed = discord.Embed(
                                                                            title="your response has timed out!",
                                                                            description="please run `r!apply` again "
                                                                                        "to restart the application "
                                                                                        "process.",
                                                                            color=0xff4747)
                                                                        await ctx.send(embed=embed)
                                                                        return
                                                                    else:
                                                                        if str(reaction.emoji) == "\U00002705":
                                                                            response["pr team"] = True
                                                                        elif str(reaction.emoji) == "\U0000274c":
                                                                            response["pr team"] = False
                                                                        embed = discord.Embed(
                                                                            title="the application is complete! your "
                                                                                  "data will now be submitted to the "
                                                                                  "staff team so they can review your "
                                                                                  "application, good luck!",
                                                                            color=0xfdfdbe)
                                                                        await ctx.send(embed=embed)
                                                                        pburl = Pastebin.create_paste(
                                                                            api_paste_private=1,
                                                                            api_paste_name=
                                                                            str(response[
                                                                                    "applicant"]),
                                                                            api_paste_code=str(response))
                                                                        channel = self.bot.fetch_channel(
                                                                            817500525968359444)
                                                                        channel.send(f'new application from {response["applicant"]}\n\nfull application here: {pburl}')

    @apply.error
    async def apply_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(title="you do not fit the requirements to be staff yet!",
                                  description="chat more in the server to get level 5 in amari!", color=0xfdfdbe)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.PrivateMessageOnly):
            await ctx.send('please use this command in my dms! be sure you have your dms opened as well')
        elif isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(title="staff applications are closed!",
                                  description="be sure to check us out for any updates!", color=0xfdfdbe)
            await ctx.send(embed=embed)
        else:
            print(f'apply command ran into an error: {error}')


def setup(bot):
    bot.add_cog(Apply(bot))