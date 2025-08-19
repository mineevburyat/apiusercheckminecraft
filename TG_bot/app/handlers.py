import asyncio
from aiogram import F, Router, types, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext


from app.reqest import register_nick
from .reg_event import registration
import app.keyboard as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Хочешь зарегистрироваться в проекте?', reply_markup=kb.start_kb)


@router.callback_query(F.data == "reg_event")  
async def start_event(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(registration.nick_name)
    await callback.message.answer("Введите ваш ник:")  
    await callback.answer()

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
    data = await state.get_data()
    status, result = register_nick(data)

    if status == 201:
        await callback.message.edit_text("✅ Событие успешно создано.")
    elif status == 0:
        await callback.message.edit_text(f"⚠️ Ошибка при подключении:\n{result}")
    else:
        # Проверим, словарь это или строка
        if isinstance(result, dict):
            msg = result.get('message', str(result))
        else:
            msg = result  # просто строка

        await callback.message.edit_text(f"❌ Ошибка при создании события (код {status}):\n{msg}")

    await state.clear()
    await callback.answer()
