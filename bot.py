import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
chat_id = os.environ.get('CHAT_ID')
dp = Dispatcher()
bot = Bot(token)


async def send_message(message):
    for i in eval(chat_id):
        print(i)
        await bot.send_message(chat_id=i, text=message)
