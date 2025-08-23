import asyncio
from aiogram import F, Router, types, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from app.reqest import register_nick
from .reg_event import registration
import app.keyboard as kb
from bot_logging.utils import log_command, log_button_click , log_revest_event



router = Router()



@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Хочешь зарегистрироваться в проекте?', reply_markup=kb.start_kb)
    log_command(message.from_user.id, message.from_user.username, "start")

@router.message(F.data == "menu")
async def start(message: Message):
    await message.answer('Хочешь зарегистрироваться в проекте?', reply_markup=kb.start_kb)


@router.callback_query(F.data == "reg_event")  
async def start_event(callback: types.CallbackQuery, state: FSMContext):
    try:
        # Логируем нажатие кнопки
        log_button_click(
            callback.from_user.id,
            callback.from_user.username,
            callback.data,
            "начало регистрации события"
        )
        
        # Логируем начало процесса регистрации
        log_revest_event(
            callback.from_user.id,
            callback.from_user.username,
            "registration_start",
            "пользователь начал регистрацию события"
        )
        
        # Устанавливаем состояние
        await state.set_state(registration.nick_name)
        
        # Отправляем сообщение
        await callback.message.answer("Введите ваш ник:")  
        
        # Подтверждаем callback
        await callback.answer("✅ Начинаем регистрацию...")
        
        # Логируем успешное начало регистрации
        log_revest_event(
            callback.from_user.id,
            callback.from_user.username,
            "registration_prompt",
            "запрос ника пользователя"
        )
        
    except Exception as e:
        # Логируем ошибку
        from bot_logging.utils import log_error
        log_error(
            "RegistrationError", 
            f"Ошибка начала регистрации: {str(e)}", 
            callback.from_user.id
        )
        await callback.answer("❌ Ошибка при начале регистрации")

@router.message(registration.nick_name)
async def nick_name(message: types.Message, state: FSMContext):
  
    await state.update_data(nick_name=message.text)
    
   
    data = await state.get_data()
    

    text = (
        "Подтвердите ваш ник\n\n"
        f"<b>Ваш ник:</b> {data['nick_name']}\n"
    )
    
    await message.answer(text, reply_markup=kb.reg_new, parse_mode="HTML")




@router.callback_query(F.data == "new")
async def confirm_event(callback: types.CallbackQuery, state: FSMContext):
    log_button_click(
        callback.from_user.id,
        callback.from_user.username,
        callback.data
    )
    data = await state.get_data()
    status, result = register_nick(data)

    
    if status == 200:
        await callback.message.edit_text("✅ Событие успешно создано.", reply_markup=kb.menu_kb )
    elif status != 200:
        await callback.message.edit_text(f"⚠️ Ошибка при подключении:\n{result}",reply_markup=kb.other)
    else:
        if isinstance(result, dict):
            msg = result.get('message', str(result))
        else:
            msg = result  

        await callback.message.edit_text(f"❌ Ошибка при создании события (код {status}):\n{msg}",reply_markup=kb.other)

    await state.clear()
    await callback.answer()
