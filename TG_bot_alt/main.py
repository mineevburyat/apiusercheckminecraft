import  asyncio
from aiogram import Bot, Dispatcher, F
from config import BOT_TOKEN
from app.handlers import router

async def main():
    print("start")
    bot = Bot(token= BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Вот так и сказочке конец!")
    
