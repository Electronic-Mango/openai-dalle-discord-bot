from lightbulb import BotApp, Context, Plugin, SlashCommand, add_checks, command, implements, option
from lightbulb.commands import MessageCommand

from command_check import check
from commands.sender import send_image

generate_plugin = Plugin("generate_plugin")


@generate_plugin.command()
@option("prompt", "Prompt to generate image for", str)
@add_checks(check)
@command("generate", "Generate image based on prompt", auto_defer=True)
@implements(SlashCommand)
async def generate(context: Context) -> None:
    await send_image(context, context.options.prompt)


@generate_plugin.command()
@add_checks(check)
@command("generate", "Generate image for given message", auto_defer=True)
@implements(MessageCommand)
async def generate_directly(context: Context) -> None:
    await send_image(context, context.options.target.content)


def load(bot: BotApp) -> None:
    bot.add_plugin(generate_plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(generate_plugin)
