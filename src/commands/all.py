from asyncio import sleep

from hikari import MessageCreateEvent
from lightbulb import BotApp, Context, Plugin, SlashCommand, add_checks, command, implements

from command_check import check
from commands.sender import send_image
from persistence import load_source_channels, store_source_channel

all_plugin = Plugin("all_plugin")
source_channels = load_source_channels()


@all_plugin.command()
@add_checks(check)
@command("start", "Start automatically generating images from prompts")
@implements(SlashCommand)
async def start(context: Context) -> None:
    await _start(context)


@all_plugin.command()
@add_checks(check)
@command("quiet_start", "Start generating images without notifying other users", ephemeral=True)
@implements(SlashCommand)
async def quiet_start(context: Context) -> None:
    await _start(context)


async def _start(context: Context) -> None:
    channel_id = context.channel_id
    source_channels.add(channel_id)
    store_source_channel(channel_id)
    await context.respond("Generating images based on all messages.")


@all_plugin.command()
@add_checks(check)
@command("stop", "Stop generating images automatically")
@implements(SlashCommand)
async def stop(context: Context) -> None:
    await _stop(context)


@all_plugin.command()
@add_checks(check)
@command("quiet_stop", "Stop generating images without notifying other users", ephemeral=True)
@implements(SlashCommand)
async def quiet_stop(context: Context) -> None:
    await _stop(context)


async def _stop(context: Context) -> None:
    channel_id = context.channel_id
    if channel_id in source_channels:
        source_channels.remove(channel_id)
    await context.respond("Automatic image generation stopped.")


@all_plugin.listener(event=MessageCreateEvent)
async def on_message(event: MessageCreateEvent) -> None:
    if await _should_skip_message(event):
        return
    channel = await event.message.fetch_channel()
    async with channel.trigger_typing():
        await sleep(0.1)  # Give the bot some time to trigger typing indicator.
        await send_image(event.message, event.content)


async def _should_skip_message(event: MessageCreateEvent) -> bool:
    return not event.is_human or not event.content or event.channel_id not in source_channels


def load(bot: BotApp) -> None:
    bot.add_plugin(all_plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(all_plugin)
