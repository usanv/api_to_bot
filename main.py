import asyncio

import uvicorn

import api
from bot import bot


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(uvicorn.run(api.app)),
        loop.create_task(bot.dp.start_polling(bot, on_shutdown=on_shutdown))
    ]
    loop.run_until_complete(asyncio.gather(*tasks))
