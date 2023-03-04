# Telegram-GPT

> This content is not affiliated with, endorsed, sponsored, or specifically
> approved by OpenAI and OpenAI is not responsible for it.

I like the web interface when I'm using chatGPT on my computer. On the other
hand I never use it on mobile (it's to much work going to web browser, sign-in
and chat). So I decide to write a very small Telegram Bot (< 80 LOC) using
[OpenAI API](https://platform.openai.com/docs/introduction) and
[aiogram](https://github.com/aiogram/aiogram).

<div align="center">
  <img alt="Example" src="https://raw.githubusercontent.com/S1M0N38/Telegram-GPT/main/example.gif"/>
</div>


## :arrow_down: Deploy

OpenAI offers some free credit for their API ($18.00 in credits for 3 month).
This bot use `gpt-3.5-turbo` endpoint for chat completions which means that
requests cost $0.002 per 1k tokens (see [blog
post](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)). So you
can deploy this bot on your machine and enjoy for three month your personal
instance of chatGPT.

1. Clone this repo and go in it: `git clone
   https://github.com/S1M0N38/Telegram-GPT.git && Telegram-GPT`
2. Create new [Telegram Bot]() obtaining a token (e.g.
   `2837489710:GJjkajsJFmmjkjDJKSekj00JKKjkjahdja2`)
3. Create new [OpenAI API key](https://platform.openai.com/account/api-keys)
   (e.g. `sk-askldj9382kjdklqLlkaj92lLanEREybjae36HSMAnd2iudj`)
4. Create new file *.env* with the following env variables (use token and
   api-key obtain from the previous steps)
```
export TELEGRAM_TOKEN="2837489710:GJjkajsJFmmjkjDJKSekj00JKKjkjahdja2"
export OPENAI_TOKEN="sk-askldj9382kjdklqLlkaj92lLanEREybjae36HSMAnd2iudj"
```
5. Load *.env* and start the bot: `source .env && python bot.py`

## :zap: Usage

Start a conversation with your bot. You can start a new conversation with
`/start`.
