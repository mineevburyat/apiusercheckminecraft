import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
import logging  # встроенный модуль Python
from bot_logging.middleware import UserActionsMiddleware  # ← ИЗМЕНИЛ
from bot_logging.logger_config import setup_logging       # ← ИЗМЕНИЛ

# Настройка логирования
setup_logging()

import configparser 
config = configparser.ConfigParser()
config.read('config.ini')

BOT_TOKEN = config['BOT']['BOT_TOKEN'].strip()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Подключаем middleware к router
    logging_middleware = UserActionsMiddleware()
    router.message.middleware(logging_middleware)
    router.callback_query.middleware(logging_middleware)
    
    dp.include_router(router)
    
    # Логируем запуск бота
    logging.getLogger('user_actions').info("🤖 Бот запускается...")
    
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.getLogger(__name__).critical(f"💥 Критическая ошибка: {e}")
        raise
    finally:
        logging.getLogger('user_actions').info("🛑 Бот остановлен")
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.getLogger('user_actions').info("⏹️ Бот остановлен пользователем")
        print("Вот так и сказочке конец!")