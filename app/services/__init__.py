from itertools import cycle
from typing import List, Optional

import discord
from discord.ext import tasks
from discord.ext.commands import Bot, HelpCommand
from discord_slash import SlashCommand


class KHSClass(Bot):
    def __init__(self, discord_token: str, bot_version: str, command_prefix: Optional[str] = None,
                 help_command: Optional[HelpCommand] = None,
                 description: str = "2021 학년도 경희고등학교 3학년 3반 디스코드 서버 용 class bot",
                 case_insensitive: bool = False, sync_commands: bool = False,
                 delete_from_unused_guilds: bool = False, sync_on_cog_reload: bool = False,
                 override_type: bool = False) -> None:
        """KHSClass Core \n
        Github: https://github.com/zeroday0619/KHSClassBOT

        :param discord_token: discord developer portal에서 발급한 토큰
        :param bot_version: KHSClassBOT Version
        :param command_prefix: command prefix
        :param help_command: help command implementation to use
        :param description: KHSClassBOT description
        :param case_insensitive: case-insensitive
        :param sync_commands: Whether to sync commands automatically. Default `False`.
        :param delete_from_unused_guilds: If the bot should make a request to set no commands for guilds that haven't got any commands registered in :class:``SlashCommand``. Default `False`.
        :param sync_on_cog_reload: Whether to sync commands on cog reload. Default `False`.
        :param override_type: Whether to override checking type of the client and try register event.
        """

        self.discord_token: str = discord_token
        self.bot_version: str = bot_version

        self._command_prefix: str = command_prefix if command_prefix else "!"
        self._description: str = description

        self._help_command = help_command
        self._case_insensitive = case_insensitive
        self._sync_commands = sync_commands
        self._delete_from_unused_guilds = delete_from_unused_guilds
        self._sync_on_cog_reload = sync_on_cog_reload
        self._override_type = override_type

        self.message: List[str] = ["!help", "@zeroday0619#4000"]
        super(KHSClass, self).__init__(
            command_prefix=self._command_prefix,
            help_command=self._help_command,
            description=self._description,
            case_insensitive=self._case_insensitive
        )
        SlashCommand(
            client=self,
            sync_commands=self._sync_commands,
            delete_from_unused_guilds=self._delete_from_unused_guilds,
            sync_on_cog_reload=self._sync_on_cog_reload,
            override_type=self._override_type
        )

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Game(next(cycle(self.message)))
        )

    def launch(self):
        self.run(self.discord_token)


