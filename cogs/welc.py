import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member.name} joined, id: {member.id}")
        embed = discord.Embed(
            description="〈<a:1_shibawave:929201546917458041>〉<@&765984584068235345> !\n<:w_heart:929202901874790440>**⬩ verify**﹐ <#763138974163795972>!*!*\n\n##　get pings & "
                        "access﹐<#763139066371244052>\n—　 add your portal﹐<#763142159800860723>\n<:w_heart:926356363381211196>　owner tools﹐<#811343776646955089>",color=0x2f3136)
        count = str(member.guild.member_count)
        ordinal = "th"
        if count[-1] == 1:
            ordinal = "st"
        elif count[-1] == 2:
            ordinal = "nd"
        elif count[-1] == 3:
            ordinal = "rd"
        embed.set_footer(text=f"・ you are our {member.guild.member_count}{ordinal} member!")
        channel = member.guild.get_channel(929200029833502740)
        await channel.send(content=f"{member.mention}", embed=embed)


def setup(bot):
    bot.add_cog(Welcome(bot))