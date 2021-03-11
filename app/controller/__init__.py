from typing import List, Optional

from discord_slash import SlashCommand

from app.config import DISCORD_BOT_TOKEN, DISCORD_BOT_VERSION
from app.error import (DISCORD_COG_LOAD_FAILED, DISCORD_COG_RELOAD_FAILED,
                       DISCORD_TOKEN_NOT_FOUND)
from app.services import KHSClass


class Controller:
    def __init__(self) -> None:
        self.DISCORD_BOT_TOKEN = DISCORD_BOT_TOKEN
        self.DISCORD_BOT_VERSION = DISCORD_BOT_VERSION
        self.controller: Optional[KHSClass] = None
        self.slash: Optional[SlashCommand] = None

    async def on_ready(self):
        print("------------------------------------------------------------")
        print(f"[*] Logged is as [{self.controller.user.name}]")
        print(f"[*] CID: {str(self.controller.user.id)}")
        print(f"[*] zeroday0619 | Copyright (C) 2021 zeroday0619")
        print("------------------------------------------------------------")
        print(f"[*] Completed!")
        await self.controller.change_status.start()

    def load_extensions(self, _cogs: List[str]):
        for extension in _cogs:
            try:
                self.controller.load_extension(extension)
            except Exception as ex:
                raise DISCORD_COG_LOAD_FAILED(extension=extension, msg=ex)

    def reload_extensions(self, _cogs: List[str]):
        for extension in _cogs:
            try:
                self.controller.reload_extension(extension)
            except Exception as ex:
                raise DISCORD_COG_RELOAD_FAILED(extension=extension, msg=ex)

    def initialize(self):
        if not self.DISCORD_BOT_TOKEN:
            raise DISCORD_TOKEN_NOT_FOUND

        self.controller = KHSClass(
            discord_token=self.DISCORD_BOT_TOKEN,
            bot_version=self.DISCORD_BOT_VERSION,
            help_command=None,
            case_insensitive=True,
        )
