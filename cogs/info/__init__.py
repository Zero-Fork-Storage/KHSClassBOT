import discord
from discord.ext import commands
from discord.ext.commands import Context


class INFO(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help", aliases=["명령어", "도움"])
    async def help(self, ctx: Context):
        embed = discord.Embed(
            title="KHSClassBOT 도움말",
            url="https://github.com/zeroday0619/KHSClassBOT",
            description="!help",
            color=0x94f5d9
        )
        embed.add_field(name="수능 d-day", value="!수능", inline=True)
        embed.set_footer(text="hosted by Microsoft Azure")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.remove_command("help")
    bot.add_cog(INFO(bot))
