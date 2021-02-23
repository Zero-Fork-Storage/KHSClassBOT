import typing
from discord.ext.commands import Bot
from app.error import DISCORD_COG_LOAD_FAILED
from app.error import DISCORD_COG_RELOAD_FAILED


class KHSClass(Bot):
    def __init__(self, discord_token: str, bot_version: str, command_prefix: typing.Optional[str] = None):

        self.discord_token: str = discord_token
        self.bot_version: str = bot_version

        self._command_prefix: str = command_prefix if command_prefix else "!"
        self._description: str = "2021 학년도 경희고등학교 3학년 3반 디스코드 서버 용 class bot"

        self._help_command = None
        self._case_insensitive = True

        super(KHSClass, self).__init__(
            command_prefix=self._command_prefix,
            description=self._description,
            help_command=self._help_command,
            case_insensitive=self.case_insensitive
        )

    def load_extensions(self, _cogs: typing.List[str]):
        for extension in _cogs:
            try:
                self.load_extension(extension)
            except Exception as ex:
                raise DISCORD_COG_LOAD_FAILED(extension=extension, msg=ex)

    def reload_extensions(self, _cogs: typing.List[str]):
        for extension in _cogs:
            try:
                self.reload_extension(extension)
            except Exception as ex:
                raise DISCORD_COG_RELOAD_FAILED(extension=extension, msg=ex)

    def launch(self):
        self.run(self.discord_token)
