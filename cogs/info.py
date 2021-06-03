import discord
from discord.ext import commands

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

def setup(bot):
    bot.add_cog(Info(bot))