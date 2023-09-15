# import asyncio
# import uvicorn
# import api
# from bot import bot
#
#
# async def on_shutdown(dp):
#     await dp.storage.close()
#     await dp.storage.wait_closed()
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     tasks = [
#         loop.create_task(uvicorn.run(api.app, host="0.0.0.0", port=8000)),
#         loop.create_task(bot.dp.start_polling(bot, on_shutdown=on_shutdown))
#     ]
#     loop.run_until_complete(asyncio.gather(*tasks))


import asyncio
import os

import uvicorn
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI

load_dotenv(find_dotenv())

# Создаем экземпляр FastAPI
app = FastAPI()

# Подключаем бота и настраиваем Dispatcher
token = os.environ.get('TOKEN')
chat_id = os.environ.get('CHAT_ID')
dp = Dispatcher()
bot = Bot(token)


# Функция для отправки сообщения через бота
async def send_message(message):
    for i in eval(chat_id):
        await bot.send_message(chat_id=i, text=message)


# Определение эндпоинта FastAPI
@app.post("/send_data/")
async def get_data(name: str, number: int):
    result = f"Received name: {name}, number: {number}"
    await send_message(f"🟢Полученно новое сообщение\nимя: {name}\nномер: {number}")
    return {"message": result}


# Функция для обработки завершения работы
async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(uvicorn.run(app='__main__:app', workers=2, reload=True)),
        loop.create_task(dp.start_polling(bot, on_shutdown=on_shutdown))
    ]
    loop.run_until_complete(asyncio.gather(*tasks))
