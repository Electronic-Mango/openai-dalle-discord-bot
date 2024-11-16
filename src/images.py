from os import getenv

from dotenv import load_dotenv
from openai import APIError, OpenAI, OpenAIError

load_dotenv()

DEFAULT_ERROR_MESSAGE = "Error occurred during image generation"

TOKEN = getenv("OPENAI_TOKEN")
MODEL = getenv("OPENAI_MODEL")

client = OpenAI(api_key=TOKEN)


def generate_image(prompt: str) -> str:
    try:
        response = client.images.generate(
            model=MODEL,
            prompt=prompt,
            response_format="url",
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except APIError as error:
        return (
            error.body.get("message", DEFAULT_ERROR_MESSAGE)
            if isinstance(error.body, dict)
            else DEFAULT_ERROR_MESSAGE
        )
    except OpenAIError:
        return DEFAULT_ERROR_MESSAGE
