from lightbulb import BotApp, Context, Plugin, SlashCommand, add_checks, command, implements, option
from lightbulb.commands import MessageCommand

from command_check import check
from images import generate_image

ask_plugin = Plugin("ask_plugin")


@ask_plugin.command()
@option("prompt", "Prompt to generate image for", str)
@add_checks(check)
@command("generate", "Generate image based on prompt", auto_defer=True)
@implements(SlashCommand)
async def ask(context: Context) -> None:
    await _generate_image(context, context.options.prompt)


@ask_plugin.command()
@add_checks(check)
@command("generate", "Generate image for given message", auto_defer=True)
@implements(MessageCommand)
async def ask_directly(context: Context) -> None:
    await _generate_image(context, context.options.target.content)


async def _generate_image(context: Context, prompt: str) -> None:
    image_url = generate_image(prompt)
    await context.respond(image_url)


def load(bot: BotApp) -> None:
    bot.add_plugin(ask_plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(ask_plugin)
