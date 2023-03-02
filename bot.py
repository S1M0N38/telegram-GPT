import json
import logging
import os
import time
from pathlib import Path

import openai
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

assert (TELEGRAM_TOKEN := os.getenv("TELEGRAM_TOKEN")), "TELEGRAM_TOKEN undefined"
assert (OPENAI_TOKEN := os.getenv("OPENAI_TOKEN")), "OPENAI_TOKEN undefined"

openai.api_key = OPENAI_TOKEN


dp = Dispatcher()
here: Path = Path(__file__).parent
conversations: Path = here / "conversations"
conversations.mkdir(exist_ok=True)


@dp.message(Command(commands=["start"]))
async def start(message: Message) -> None:
    if message.from_user is not None:
        (conversations / str(message.from_user.id)).mkdir(exist_ok=True)
        (
            conversations / str(message.from_user.id) / f"{int(time.time())}.ndjson"
        ).touch()

    await message.answer(
        (
            "Welcome this is a chat-bot powered by chatGPT\n"
            "• /start: start a new conversation with the bot\n"
            # Add here other commands
        ),
    )


@dp.message()
async def echo_handler(message: Message) -> None:
    if message.from_user is not None and message.text is not None:
        query: dict = {"role": "user", "content": message.text}
        path: Path = sorted((conversations / str(message.from_user.id)).glob("*"))[-1]

        with open(path) as f:
            history: list[dict] = [json.loads(line) for line in f.readlines()]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[*history, query],
            user=str(message.from_user.id),
        )

        response: dict = completion["choices"][0]["message"]

        with open(path, "a") as f:
            f.write(f"{json.dumps(query)}\n")
            f.write(f"{json.dumps(response)}\n")

        await message.answer(response["content"])


def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp.run_polling(bot)


if __name__ == "__main__":
    # import sys

    logging.basicConfig(
        level=logging.INFO,
        filename=here / "bot.log",
        # stream=sys.stdout,
    )
    main()
