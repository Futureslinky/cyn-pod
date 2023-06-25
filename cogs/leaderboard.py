import discord
from discord.ext import commands

class leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def leaderboard(self, ctx):
        embed = discord.Embed(title="Leaderboard", description="Here is the cuurent leaderboard. Note that is may have not been updated", color=0x2B2D31)
        embed.set_image(url="https://keepthescore.com/preview.png?token=bbxzbvbzkfclr")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(leaderboard(bot))
