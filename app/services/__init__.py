import discord
from typing import List
from typing import Optional
from itertools import cycle
from discord.ext import tasks
from discord.ext.commands import Bot
from discord.ext.commands import HelpCommand


class KHSClass(Bot):
    def __init__(
            self,
            discord_token: str,
            bot_version: str,
            command_prefix: Optional[str] = None,
            help_command: Optional[HelpCommand] = None,
            description: str = "2021 학년도 경희고등학교 3학년 3반 디스코드 서버 용 class bot",
            case_insensitive: bool = False
    ) -> None:
        """KHSClass Core \n
        Github: https://github.com/zeroday0619/KHSClassBOT

        :param discord_token: discord developer portal에서 발급한 토큰
        :param bot_version: KHSClassBOT Version
        :param command_prefix: command prefix
        :param help_command: help command implementation to use
        :param description: KHSClassBOT description
        :param case_insensitive: case-insensitive
        """

        self.discord_token: str = discord_token
        self.bot_version: str = bot_version

        self._command_prefix: str = command_prefix if command_prefix else "!"
        self._description: str = description

        self._help_command = help_command
        self._case_insensitive = case_insensitive

        self.message: List[str] = ["!help", "@zeroday0619#4000"]

        super(KHSClass, self).__init__(
            command_prefix=self._command_prefix,
            help_command=self._help_command,
            description=self._description,
            case_insensitive=self._case_insensitive
        )

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Game(next(cycle(self.message)))
        )

    def launch(self):
        self.run(self.discord_token)




