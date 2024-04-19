from os import getenv

from dotenv import load_dotenv
from hikari import Intents
from lightbulb import BotApp

from commands.all import load as load_all
from commands.generate import load as load_ask

INTENTS = Intents.MESSAGE_CONTENT | Intents.DM_MESSAGES | Intents.GUILD_MESSAGES
TOKEN = getenv("BOT_TOKEN")
LOG_LEVEL = "DEBUG"


def main():
    load_dotenv()
    bot = BotApp(token=TOKEN, intents=INTENTS, logs=LOG_LEVEL)
    load_all(bot)
    load_ask(bot)
    bot.run()


if __name__ == "__main__":
    main()
