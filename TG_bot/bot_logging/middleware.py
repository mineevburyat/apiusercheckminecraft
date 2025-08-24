from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Dict, Any, Awaitable
import logging

class UserActionsMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, event: Any, data: Dict[str, Any]) -> Any:
        try:
            self._log_incoming_event(event)
            return await handler(event, data)
        except Exception as e:
            logging.error(f"Ошибка обработки: {e}")
            raise

    def _log_incoming_event(self, event: Any):
        user_info = self._get_user_info(event)
        
        if isinstance(event, Message):
            if event.text:
                logging.getLogger('user_actions').info(f"СООБЩЕНИЕ | {user_info} | Текст: {event.text}")
            elif event.photo:
                logging.getLogger('user_actions').info(f"ФОТО | {user_info}")
            elif event.document:
                logging.getLogger('user_actions').info(f"ФАЙЛ | {user_info} | {event.document.file_name}")
                
        elif isinstance(event, CallbackQuery):
            logging.getLogger('user_actions').info(f"INLINE КНОПКА | {user_info} | Данные: {event.data}")

    def _get_user_info(self, event: Any) -> str:
        user = getattr(event, 'from_user', None) or getattr(getattr(event, 'message', None), 'from_user', None)
        if user:
            return f"ID: {user.id} | Имя: {user.first_name or ''} | @{user.username or 'нет'}"
        return "Неизвестный пользователь"