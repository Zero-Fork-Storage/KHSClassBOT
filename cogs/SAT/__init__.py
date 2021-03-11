import datetime

import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext


class SAT(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="수능")
    async def d_day_counter(self, ctx: SlashContext):
        """수능 d-day 카운터"""
        KST = datetime.timezone(datetime.timedelta(hours=9))
        today = datetime.datetime.now(tz=KST).date()
        SAT_DAY = datetime.date(2021, 11, 17)
        d_day = SAT_DAY - today
        embed = discord.Embed(
            title="수능 d-day 카운터",
            url="https://www.kice.re.kr/main.do?s=suneung",
            description="2022학년도 대학수학능력시험 d-day 카운터",
            color=0x0129EF,
        )
        embed.add_field(name="2022 수능까지", value=f"{d_day.days}일 남았습니다", inline=False)
        embed.set_footer(text="hosted by Microsoft Azure")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(SAT(bot))
