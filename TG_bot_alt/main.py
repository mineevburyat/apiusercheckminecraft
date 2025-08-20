import  asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router

import configparser 
config = configparser.ConfigParser()
config.read('config.ini')

BOT_TOKEN = config['BOT']['BOT_TOKEN'].strip()

async def main():
    bot = Bot(token= BOT_TOKEN)
    print("start", BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Вот так и сказочке конец!")
    
