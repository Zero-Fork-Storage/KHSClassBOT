import os
import typing

REDIS_PORT: typing.Optional[int] = os.environ.get("REDIS_PORT")
NEIS_API_KEY: typing.Optional[str] = os.environ.get("NEIS_API_KEY")
DISCORD_BOT_TOKEN: typing.Optional[str] = os.environ.get("DISCORD_BOT_TOKEN")
DISCORD_BOT_VERSION: typing.Optional[str] = os.environ.get("DISCORD_BOT_VERSION")
