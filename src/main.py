from os import getenv

from dotenv import load_dotenv
from hikari import Intents
from lightbulb import BotApp

from commands.all import load as load_all
from commands.generate import load as load_ask

load_dotenv()

INTENTS = Intents.MESSAGE_CONTENT | Intents.DM_MESSAGES | Intents.GUILD_MESSAGES

bot = BotApp(token=getenv("BOT_TOKEN"), intents=INTENTS, logs="DEBUG")

load_all(bot)
load_ask(bot)

bot.run()
