from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [424472476106489856]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS,
            intents=Intents.all()
        )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running Chopper...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Chopper connected.")

    async def on_disconnect(self):
        print("Chopper disconnected.")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(704165535226527765)
            print("Chopper ready.")

        else:
            print("Chopper reconnected.")

    async def on_message(self, message):
        pass

bot = Bot()
