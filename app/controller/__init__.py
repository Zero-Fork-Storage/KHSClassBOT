from discord.ext.commands import Context

from typing import Optional
from app.services import KHSClass
from app.config import DISCORD_BOT_TOKEN
from app.config import DISCORD_BOT_VERSION
from app.error import DISCORD_TOKEN_NOT_FOUND


class Controller:
    def __init__(self) -> None:
        self.DISCORD_BOT_TOKEN = DISCORD_BOT_TOKEN
        self.DISCORD_BOT_VERSION = DISCORD_BOT_VERSION
        self.core: Optional[KHSClass] = None

    def initialize(self):
        if not self.DISCORD_BOT_TOKEN:
            raise DISCORD_TOKEN_NOT_FOUND

        self.core = KHSClass(
            discord_token=self.DISCORD_BOT_TOKEN,
            bot_version=self.DISCORD_BOT_VERSION
        )