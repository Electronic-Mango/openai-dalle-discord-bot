from hikari import URL, PartialMessage
from lightbulb import Context

from images import generate_image


async def send_image(response_context: PartialMessage | Context, prompt: str) -> None:
    response, valid = generate_image(prompt)
    await response_context.respond(URL(response) if valid else response)
