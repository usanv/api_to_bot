from fastapi import FastAPI
import bot
app = FastAPI()


@app.post("/send_data/")
async def get_data(name: str, number: int):
    result = f"Received name: {name}, number: {number}"
    await bot.send_message(f"🟢Полученно новое сообщение\nимя: {name}\nномер: {number}")
    return {"message": result}
