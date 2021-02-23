import discord
from itertools import cycle
from discord.ext import tasks
from app.controller import Controller


class DiscordClient:
    def __init__(self):
        self.message = cycle(["!help", "@zeroday0619#4000"])
        self.client = Controller()
        self.co(self.on_ready)

    def co(self, coro):
        self.client.initialize()
        self.client.core.event(coro)

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.core.change_presence(
            status=discord.Status.online,
            activity=discord.Game(next(self.message))
        )

    async def on_ready(self):
        print("------------------------------------------------------------")
        print(f"[*] Logged is as [{self.client.core.user.name}]")
        print(f"[*] CID: {str(self.client.core.user.id)}")
        print(f"[*] zeroday0619 | Copyright (C) 2021 zeroday0619")
        print("------------------------------------------------------------")
        print(f'[*] Completed!')
        await self.change_status.start()

    def run(self):
        self.client.core.launch()


class MainSystem:
    def __init__(self):
        print("initializing main program")

    def run(self):
        self.main()

    def main(self):
        objDiscordClient = DiscordClient()
        objDiscordClient.run()
