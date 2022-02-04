
# Code written by unknown <3

import discord
from discord.ext import commands
import discord.utils 
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_components import *
from discord_slash.model import ButtonStyle
import logging
import random
import string
import asyncio
import os
import time
import json

log = logging.getLogger(__name__)

json_file = open("settings.json")
config = json.load(json_file)
json_file.close()

#captcha modules
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha

#setting font
image = ImageCaptcha(width = 280, height = 90)
audio = AudioCaptcha()

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def sendverification(self, ctx):
            choose = create_select(
                options=[
                    create_select_option("Image Verification", value="image", emoji="📷"),
                    create_select_option("Audio Verification", value="audio", emoji="🎧"),
                ],
                placeholder="What type of verification should I send you?",
                min_values=1, 
                max_values=1 
            )
            action_row = create_actionrow(choose)

            embed = discord.Embed(description="idk yall put your fancy stuff here",color=0x2f3136)
            await ctx.send(embed=embed, components=[action_row])    


    @commands.Cog.listener()
    async def on_component(self, ctx: ComponentContext):
        def check(m):
            return m.author == ctx.author

        if ctx.selected_options[0] == 'audio':
            await ctx.send('Sent you the verification in dms!', hidden=True)

            sampleint = random.randrange(1111,9999)
            data = audio.generate(f'{sampleint}')
            audio.write(f'{sampleint}', f'captchas/{ctx.author.id}.wav')
            await ctx.author.send(content='Here is the audio for you!\n Please send a message to the bot with the code you hear', file=discord.File(f'captchas/{ctx.author.id}.wav', filename='audio.wav'))
            try:
                code = await self.bot.wait_for(event="message", check=check, timeout=900)
                role = ctx.guild.get_role(config["RoleAfterCaptha"])
                if f'{sampleint}' == code.content:
                    await ctx.author.add_roles(role) 
                    await ctx.author.send('You got the right code! You got the verified role')
                else:
                    await ctx.author.send('I don\'t seem to know this code... Please try again!')
                    time.sleep(1)
                    try:
                        sampleint = random.randrange(1111,9999)
                        data = audio.generate(f'{sampleint}')
                        audio.write(f'{sampleint}', f'captchas/{ctx.author.id}.wav')

                        await ctx.author.send(content='Here is the audio for you!\n Please send a message to the bot with the code you hear', file=discord.File(f'captchas/{ctx.author.id}.wav', filename='audio.wav'))
                        code2 = await self.bot.wait_for(event="message", check=check, timeout=900)

                        if code2.content == f'{sampleint}':
                            await ctx.author.send('You got the right code! You got the verified role')
                            await ctx.author.add_roles(role) 
                        else:
                            await ctx.author.send(f'I don\'t know this code either...')

                    except asyncio.TimeoutError:
                        embed = discord.Embed(
                            title="your response has timed out!",
                            description="please choose your option [here](own setting) here!",
                            color=0x2f3136,
                        )
                        await ctx.send(embed=embed)     

                time.sleep(3)           
                os.remove(f'captchas/{ctx.author.id}.wav')
            except asyncio.TimeoutError:
                embed = discord.Embed(
                    title="your response has timed out!",
                    description="please choose your option [here](own setting) here!",
                    color=0x2f3136,
                )
                await ctx.send(embed=embed)

        if ctx.selected_options[0] == 'image': 
            await ctx.send('Sent you the verification in dms!', hidden=True)

            digits = random.choices(string.digits, k=2)
            letters = random.choices(string.ascii_uppercase, k=4)
            samplearr = random.sample(digits + letters, 6)
            sample = "".join(str(x) for x in samplearr)

            data = image.generate(sample) 
            image.write(sample, f'captchas/{ctx.author.id}.png')

            await ctx.author.send(content='Please type the code you see in the image below!', file=discord.File(f'captchas/{ctx.author.id}.png'))
                
            try:
                code = await self.bot.wait_for(event="message", check=check, timeout=900)
                role = ctx.guild.get_role(config["RoleAfterCaptha"])

                if sample == code.content:
                    await ctx.author.add_roles(role) 
                    await ctx.author.send('You got the right code! You got the verified role')
                else:
                    await ctx.author.send('I don\'t seem to know this code... Please try again!')
                    time.sleep(1)
                    try:
                        digits = random.choices(string.digits, k=2)
                        letters = random.choices(string.ascii_uppercase, k=4)
                        samplearr = random.sample(digits + letters, 6)
                        sample = "".join(str(x) for x in samplearr)
                        data = image.generate(sample) 
                        image.write(sample, f'captchas/{ctx.author.id}.png')

                        await ctx.author.send(content='Please type the code you see in the image below!', file=discord.File(f'captchas/{ctx.author.id}.png'))
                        code2 = await self.bot.wait_for(event="message", check=check, timeout=900)

                        if code2.content == sample:
                            await ctx.author.send('You got the right code! You got the verified role')
                            await ctx.author.add_roles(role) 
                        else:
                            await ctx.author.send(f'I don\'t know this code either...')

                    except asyncio.TimeoutError:
                        embed = discord.Embed(
                            title="your response has timed out!",
                            description="please choose your option [here](own setting) here!",
                            color=0xFF4747,
                        )
                        await ctx.send(embed=embed)     

                time.sleep(3)           
                os.remove(f'captchas/{ctx.author.id}.png')
            except asyncio.TimeoutError:
                embed = discord.Embed(
                    title="your response has timed out!",
                    description="please choose your option [here](own setting) here!",
                    color=0x2f3136,
                )
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Verification(bot))