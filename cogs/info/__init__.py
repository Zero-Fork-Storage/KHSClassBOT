import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord_slash import SlashContext, cog_ext


class INFO(commands.Cog):
    """KHSClassBOT System Information"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx: Context):
        embed = discord.Embed(
            title="Pachirisu 도움말",
            url="https://github.com/zeroday0619/KHSClassBOT",
            color=0x94f5d9
        )
        embed.add_field(
            name="/about",
            value="Introduce of Pachirisu",
            inline=False
        )
        embed.add_field(
            name="/수능",
            value="2022학년도 대학수학능력시험 d-day counter",
            inline=False
        )
        embed.add_field(
            name="/조식",
            value="오늘 조식 메뉴",
            inline=True
        )
        embed.add_field(
            name="/중식",
            value="오늘 중식 메뉴",
            inline=True
        )
        embed.add_field(
            name="/석식",
            value="오늘 석식 메뉴",
            inline=True
        )
        embed.set_footer(text="hosted by Microsoft Azure")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="about")
    async def about(self, ctx: SlashContext):
        """!about"""
        embed = discord.Embed(
            color=0x60f6c4
        )
        embed.set_author(
            name="Pachirisu",
            url="https://github.com/zeroday0619/KHSClassBOT"
        )
        embed.add_field(
            name="About...",
            value="2021학년도 경희고등힉교 3학년 3반 디스코드 서버를 위해 개발한 디스코드 봇.",
            inline=True
        )
        embed.add_field(
            name="Repository",
            value="[>> zeroday0619/KHSClassBOT](https://github.com/zeroday0619/KHSClassBOT)",
            inline=False
        )
        embed.add_field(
            name="License",
            value="Distributed under [MIT License](https://github.com/zeroday0619/KHSClassBOT/blob/main/LICENSE).",
            inline=True
        )
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.remove_command("help")
    bot.add_cog(INFO(bot))
