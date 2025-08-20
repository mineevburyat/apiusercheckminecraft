from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


start_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='конечно!!!!' , callback_data='reg_event')]])


reg_new = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Правильно', callback_data='new')]])
