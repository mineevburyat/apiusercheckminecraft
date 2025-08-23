import logging

# Глобальные логгеры
user_actions_logger = logging.getLogger('user_actions')
main_logger = logging.getLogger(__name__)

def log_button_click(user_id: int, username: str, button_data: str, context: str = ""):
    """Логирование нажатия кнопки"""
    user_info = f"ID: {user_id} | @{username or 'нет'}"
    log_msg = f"КНОПКА | {user_info} | Данные: {button_data}"
    if context:
        log_msg += f" | Контекст: {context[:50]}..."
    user_actions_logger.info(log_msg)

def log_command(user_id: int, username: str, command: str, args: str = ""):
    """Логирование команды"""
    user_info = f"ID: {user_id} | @{username or 'нет'}"
    full_cmd = f"/{command} {args}" if args else f"/{command}"
    user_actions_logger.info(f"КОМАНДА | {user_info} | {full_cmd}")

def log_revest_event(user_id: int, username: str, event_type: str, details: str):
    """Логирование событий из модуля revest"""
    user_info = f"ID: {user_id} | @{username or 'нет'}"
    user_actions_logger.info(f"🔄 REVEST | {user_info} | {event_type}: {details}")

def log_keyboard_action(user_id: int, username: str, action: str, keyboard_type: str):
    """Логирование действий с клавиатурой"""
    user_info = f"ID: {user_id} | @{username or 'нет'}"
    user_actions_logger.info(f"КЛАВИАТУРА | {user_info} | {action} | Тип: {keyboard_type}")

def log_error(error_type: str, error_msg: str, user_id: int = None):
    """Логирование ошибок"""
    if user_id:
        main_logger.error(f"ОШИБКА | User {user_id} | {error_type}: {error_msg}")
    else:
        main_logger.error(f"ОШИБКА | {error_type}: {error_msg}")