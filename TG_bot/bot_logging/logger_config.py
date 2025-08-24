import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    """Настройка логирования для всего проекта"""
    
    if not os.path.exists('../logs'):
        os.makedirs('../logs')
    
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Основной лог
    main_handler = RotatingFileHandler(
        '../logs/bot.log',
        maxBytes=5*1024*1024,
        backupCount=3,
        encoding='utf-8'
    )
    main_handler.setFormatter(formatter)
    
    # Лог действий пользователя
    user_handler = RotatingFileHandler(
        '../logs/user_actions.log',
        maxBytes=5*1024*1024,
        backupCount=3,
        encoding='utf-8'
    )
    user_handler.setFormatter(formatter)
    
    # Консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Базовая настройка
    logging.basicConfig(
        level=logging.INFO,
        handlers=[main_handler, console_handler]
    )
    
    # Логгер для действий пользователя
    user_logger = logging.getLogger('user_actions')
    user_logger.setLevel(logging.INFO)
    user_logger.handlers.clear()
    user_logger.addHandler(user_handler)
    user_logger.addHandler(console_handler)
    user_logger.propagate = False
    
    # Уменьшаем логи библиотек
    logging.getLogger('aiogram').setLevel(logging.WARNING)
    logging.getLogger('asyncio').setLevel(logging.WARNING)
    
    return user_logger

# Инициализация при импорте
user_actions_logger = setup_logging()