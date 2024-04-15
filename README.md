# Simple OpenAI image model Discord bot

A simple and unofficial Discord bot wrapping [OpenAI API](https://openai.com/blog/openai-api/) image models (like [DALL·E](https://openai.com/dall-e-3)), build with [`hikari`](https://github.com/hikari-py/hikari) and [`lightbulb`](https://github.com/tandemdude/hikari-lightbulb)!

Bot works on servers for everyone, it will respond to DMs only for bot owner.



## Requirements

This bot was built with `Python 3.12`, [`hikari`](https://github.com/hikari-py/hikari), [`lightbulb`](https://github.com/tandemdude/hikari-lightbulb) and [`openai-python`](https://github.com/openai/openai-python).
Full list of Python requirements is in the `requirements.txt` file, you can use it to install all of them.



## Bot permissions

### Message content

This bot requires **message content privileged gateway intent** to function correctly.
This is required as bot can respond to all messages in a given channel.

You can enable this content for the whole bot in [Discord Developer Portal](https://discord.com/developers/applications) and specific bot settings.

Currently, bot won't even start without this privileged intent enabled.



## Configuration

Configuration is done through a `.env` file. You can copy example file `.env.example` as `.env` and fill required parameters.

```commandline
cp .env.example .env
```


### Discord bot

### Discord bot

Only required parameter is a bot token

```dotenv
BOT_TOKEN='<your secret bot token>'
```


You can also optionally specify file in which all target channels for `start` command can be stored:

```dotenv
SOURCES_PERSISTENCE_FILE='<path to basic persistence file>'
```

Bot will store all channel IDs where automatic responding is configured in this file.

After bot is restarted (if the specified file still exists and wasn't modified) it will keep responding in previously configured channels.


### OpenAI API

There are two required parameters - [API key](https://platform.openai.com/account/api-keys) and [used model](https://platform.openai.com/docs/models/dall-e).

```dotenv
OPENAI_TOKEN='<your secret API key>'
OPENAI_MODEL='dall-e-3 or dall-e-2'
```

Through `.env` you can also configure level of logging of OpenAI API through `OPENAI_LOG` parameter.
You can set it to `debug` or `info`.
```dotenv
OPENAI_LOG='debug or info'
```



## Commands

All commands work on servers for everyone and in DMs for bot owner.

* `/start` - start generating images for all messages in current channel
* `/quiet_start` - start generating images for all messages in current channel without notifying other users
* `/stop` - stop generating images automatically
* `/quiet_stop` - stop generating images automatically without notifying other users
* `/generate` - generate image based on given prompt
* `generate` - **message command**, generate image based on selected message



## Running the bot

You can run the bot from the source code directly, or in a Docker container.


### From source code

1. Create a Discord bot
2. Create [OpenAI API key](https://platform.openai.com/account/api-keys)
3. Install all packages from `requirements.txt`
4. Fill `.env` file
5. Run `main.py` file with Python


### Docker

1. Create a Discord bot
2. Create [OpenAI API key](https://platform.openai.com/account/api-keys)
3. Fill `.env` file
4. Run `docker compose up -d --build` in terminal

Note that `.env` file is used only for loading environment variables into Docker container through compose.
The file itself isn't added to the container.

When using Docker the bot will automatically store channel IDs for purposes of `start` command in `persistence` file located in project root.



## Disclaimer

This bot is in no way affiliated, associated, authorized, endorsed by, or in any way officially connected with OpenAI.
This is an independent and unofficial project.
Use at your own risk.
