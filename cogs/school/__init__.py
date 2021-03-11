import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord_slash import SlashContext, cog_ext

from app.extension import NEISClient


class School(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cafeteria = NEISClient()

    async def meal_filter(self, nt: str):
        meal = await self.cafeteria.cafeteria()
        for bob in meal:
            if bob.get(nt):
                return bob.get(nt)
        return "NEIS API: 해당하는 데이터가 없습니다."

    @cog_ext.cog_slash(name="조식")
    async def get_meal_a(self, ctx: SlashContext):
        """오늘 조식 메뉴"""
        meal = await self.meal_filter("조식")
        embed = discord.Embed(title="오늘의 급식", color=0x0129EF)
        embed.add_field(name="menu", value=f"""```{meal}```""", inline=False)
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="중식")
    async def get_meal_b(self, ctx: SlashContext):
        """오늘 중식 메뉴"""
        meal = await self.meal_filter("중식")
        embed = discord.Embed(title="오늘의 급식", color=0x0129EF)
        embed.add_field(name="menu", value=f"""```{meal}```""", inline=False)
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="석식")
    async def get_meal_c(self, ctx: SlashContext):
        """오늘 석식 메뉴"""
        meal = await self.meal_filter("석식")
        embed = discord.Embed(title="오늘의 급식", color=0x0129EF)
        embed.add_field(name="menu", value=f"""```{meal}```""", inline=False)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(School(bot))
