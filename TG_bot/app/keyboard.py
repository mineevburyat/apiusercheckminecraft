from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from bot_logging.utils import log_keyboard_action


start_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='регистрация' , callback_data='reg_event')]])

menu_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='регистрация' , callback_data='menu')]])


reg_new = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Правильно', callback_data='new')]])

other = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'Зарегистрироваться заново', callback_data='new')],
                                              [InlineKeyboardButton(text = 'Вернуться в меню', callback_data= 'menu')]])



