from app.controller import Controller
from app.services import KHSClass


class DiscordClient(Controller):
    def __init__(self):
        super(DiscordClient, self).__init__()

        self.event(self.on_ready)

    def event(self, coro):
        self.initialize()
        self.controller.event(coro)

    def _run(self):
        self.controller.launch()


class KHSClassBOT(DiscordClient):
    def __init__(self):
        print("initializing main program")
        super(KHSClassBOT, self).__init__()

    def add_presence(self, message: str):
        self.controller.message.append(message)

    def run(self):
        self._run()
