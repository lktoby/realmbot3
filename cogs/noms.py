import discord
from discord.ext import commands
import asyncio
import datetime

class Noms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    global isopen

    @commands.command(name='nom status')
    async def nomstatus(self, ctx, value):
        isopen = True
        if value == "true":
            isopen = True
            await ctx.send('application status has been set to: **true**.')
        elif value == "false":
            isopen = False
            await ctx.send('application status has been set to: **false**.')
        else:
            await ctx.send('toby remember the values are "true" and "false"')

    @commands.command(name='nominate')
    @commands.dm_only()
    async def nominate(self, ctx):
        global isopen
        isopen = True
        if isopen == False:
            ctx.command.update(enabled=False)
            return
        response = {
            "nominator": f"{ctx.message.author.name}#{ctx.message.author.discriminator}, id: {ctx.message.author.id}"}
        embed = discord.Embed(title="welcome to the realm of portals apm of the month nomination!!",
                              description="please send anything to proceed to the form.",
                              color=0xfdfdbe)
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
        else: # new pm
            embed = discord.Embed(title="who do you think should be the __new pm of july__?", description="please make sure they have the 'new apm' role.",color=0xfdfdbe)
            embed.set_footer(text="e.g. toby#0508, 477096301364903936")
            await ctx.send(embed=embed)
            try:
                r1 = await self.bot.wait_for(event='message', check=check, timeout=900)
                response['new pm'] = r1.content
            except asyncio.TimeoutError:
                embed = discord.Embed(title="your response has timed out!",
                                      description="please run `r!apply` again to restart the application process.",
                                      color=0xff4747)
                await ctx.send(embed=embed)
                return
            else:  # new pm reason
                embed = discord.Embed(title="__why__ do you think they should be the __new pm of july__?",
                                      description="please make sure they have the 'new apm' role.", color=0xfdfdbe)
                await ctx.send(embed=embed)
                try:
                    r2 = await self.bot.wait_for(event='message', check=check, timeout=900)
                    response['new pm reason'] = r2.content
                except asyncio.TimeoutError:
                    embed = discord.Embed(title="your response has timed out!",
                                          description="please run `r!apply` again to restart the application process.",
                                          color=0xff4747)
                    await ctx.send(embed=embed)
                    return
                else:  # new am
                    embed = discord.Embed(title="who do you think should be the __new am of july__?",
                                          description="please make sure they have the 'new apm' role.", color=0xfdfdbe)
                    embed.set_footer(text="e.g. toby#0508, 477096301364903936")
                    await ctx.send(embed=embed)
                    try:
                        r3 = await self.bot.wait_for(event='message', check=check, timeout=900)
                        response['new am'] = r3.content
                    except asyncio.TimeoutError:
                        embed = discord.Embed(title="your response has timed out!",
                                              description="please run `r!apply` again to restart the application process.",
                                              color=0xff4747)
                        await ctx.send(embed=embed)
                        return
                    else:  # new am reason
                        embed = discord.Embed(title="__why__ do you think they should be the __new am of july__?",
                                              description="please make sure they have the 'new apm' role.",
                                              color=0xfdfdbe)
                        await ctx.send(embed=embed)
                        try:
                            r4 = await self.bot.wait_for(event='message', check=check, timeout=900)
                            response['new am reason'] = r4.content
                        except asyncio.TimeoutError:
                            embed = discord.Embed(title="your response has timed out!",
                                                  description="please run `r!apply` again to restart the application process.",
                                                  color=0xff4747)
                            await ctx.send(embed=embed)
                            return
                        else:  # exp pm
                            embed = discord.Embed(title="who do you think should be the __experienced pm of july__?",
                                                  description="please make sure they have the 'experienced apm' role.",
                                                  color=0xfdfdbe)
                            embed.set_footer(text="e.g. toby#0508, 477096301364903936")
                            await ctx.send(embed=embed)
                            try:
                                r5 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                response['exp pm'] = r5.content
                            except asyncio.TimeoutError:
                                embed = discord.Embed(title="your response has timed out!",
                                                      description="please run `r!apply` again to restart the application process.",
                                                      color=0xff4747)
                                await ctx.send(embed=embed)
                                return
                            else:  # exp pm reason
                                embed = discord.Embed(title="__why__ do you think they should be the __experienced pm of july__?",
                                                      description="please make sure they have the 'experienced apm' role.",
                                                      color=0xfdfdbe)
                                await ctx.send(embed=embed)
                                try:
                                    r6 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                    response['exp pm reason'] = r6.content
                                except asyncio.TimeoutError:
                                    embed = discord.Embed(title="your response has timed out!",
                                                          description="please run `r!apply` again to restart the application process.",
                                                          color=0xff4747)
                                    await ctx.send(embed=embed)
                                    return
                                else:  # exp am
                                    embed = discord.Embed(
                                        title="who do you think should be the __experienced am of july__?",
                                        description="please make sure they have the 'experienced apm' role.",
                                        color=0xfdfdbe)
                                    embed.set_footer(text="e.g. toby#0508, 477096301364903936")
                                    await ctx.send(embed=embed)
                                    try:
                                        r7 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                        response['exp am'] = r7.content
                                    except asyncio.TimeoutError:
                                        embed = discord.Embed(title="your response has timed out!",
                                                              description="please run `r!apply` again to restart the application process.",
                                                              color=0xff4747)
                                        await ctx.send(embed=embed)
                                        return
                                    else:  # exp am reason
                                        embed = discord.Embed(
                                            title="__why__ do you think they should be the __experienced am of july__?",
                                            description="please make sure they have the 'experienced apm' role.",
                                            color=0xfdfdbe)
                                        await ctx.send(embed=embed)
                                        try:
                                            r8 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                            response['exp am reason'] = r8.content
                                        except asyncio.TimeoutError:
                                            embed = discord.Embed(title="your response has timed out!",
                                                                  description="please run `r!apply` again to restart the application process.",
                                                                  color=0xff4747)
                                            await ctx.send(embed=embed)
                                            return
                                        else:  # overall pm
                                            embed = discord.Embed(
                                                title="who do you think should be the __overall pm of july__?",
                                                description="please make sure they have the 'linked apm' role.",
                                                color=0xfdfdbe)
                                            embed.set_footer(text="e.g. toby#0508, 477096301364903936")
                                            await ctx.send(embed=embed)
                                            try:
                                                r9 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                                response['overall pm'] = r9.content
                                            except asyncio.TimeoutError:
                                                embed = discord.Embed(title="your response has timed out!",
                                                              description="please run `r!apply` again to restart the application process.",
                                                              color=0xff4747)
                                                await ctx.send(embed=embed)
                                                return
                                            else:  # overall pm reason
                                                embed = discord.Embed(
                                                    title="__why__ do you think they should be the __overall pm of july__?",
                                                    description="please make sure they have the 'linked apm' role.",
                                                    color=0xfdfdbe)
                                                await ctx.send(embed=embed)
                                                try:
                                                   r10 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                                   response['overall pm reason'] = r10.content
                                                except asyncio.TimeoutError:
                                                   embed = discord.Embed(title="your response has timed out!",
                                                                  description="please run `r!apply` again to restart the application process.",
                                                                  color=0xff4747)
                                                   await ctx.send(embed=embed)
                                                   return
                                                else:  # overall am
                                                    embed = discord.Embed(
                                                        title="who do you think should be the __overall am of july__?",
                                                        description="please make sure they have the 'linked apm' role.",
                                                        color=0xfdfdbe)
                                                    embed.set_footer(text="e.g. toby#0508, 477096301364903936")
                                                    await ctx.send(embed=embed)
                                                    try:
                                                        r11 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                                        response['overall am'] = r11.content
                                                    except asyncio.TimeoutError:
                                                        embed = discord.Embed(title="your response has timed out!",
                                                              description="please run `r!apply` again to restart the application process.",
                                                              color=0xff4747)
                                                        await ctx.send(embed=embed)
                                                        return
                                                    else:  # overall am reason
                                                        embed = discord.Embed(
                                                            title="__why__ do you think they should be the __overall pm of july__?",
                                                            description="please make sure they have the 'linked apm' role.",
                                                            color=0xfdfdbe)
                                                        await ctx.send(embed=embed)
                                                        try:
                                                            r12 = await self.bot.wait_for(event='message', check=check, timeout=900)
                                                            response['overall am reason'] = r12.content
                                                        except asyncio.TimeoutError:
                                                            embed = discord.Embed(title="your response has timed out!",
                                                                  description="please run `r!apply` again to restart the application process.",
                                                                  color=0xff4747)
                                                            await ctx.send(embed=embed)
                                                            return
                                                        else:
                                                            embed = discord.Embed(title=f'nomination from {response["nominator"]}', color=0xfdfdbe, timestamp=datetime.datetime.utcnow())
                                                            embed.add_field(name='nomination for __new pm__:', value=response['new pm'], inline=False)
                                                            embed.add_field(name='reason:', value=response['new pm reason'], inline=False)
                                                            embed.add_field(name='nomination for __new am__:', value=response['new am'], inline=False)
                                                            embed.add_field(name='reason:', value=response['new am reason'], inline=False)
                                                            embed.add_field(name='nomination for __experienced pm__:', value=response['exp pm'], inline=False)
                                                            embed.add_field(name='reason:', value=response['exp pm reason'], inline=False)
                                                            embed.add_field(name='nomination for __experienced am__:', value=response['exp am'], inline=False)
                                                            embed.add_field(name='reason:', value=response['exp am reason'], inline=False)
                                                            embed.add_field(name='nomination for __overall pm__:', value=response['overall pm'], inline=False)
                                                            embed.add_field(name='reason:', value=response['overall pm reason'], inline=False)
                                                            embed.add_field(name='nomination for __overall am__:', value=response['overall am'], inline=False)
                                                            embed.add_field(name='reason:', value=response['overall am reason'], inline=False)
                                                            await ctx.send(content='your final picks are listed as follows:',embed=embed)
                                                            channel = self.bot.get_channel(846822917627052092)
                                                            await channel.send(embed=embed)
                                                            embed = discord.Embed(
                                                                title="thank you for your submission!",
                                                                description="your submission is only visible to our admins and our anonymous judges panel.",
                                                                color=0xfdfdbe)
                                                            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Noms(bot))