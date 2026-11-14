from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.database as db
import app.states as st


router = Router()


@router.message(CommandStart())
async def cmdstart(message: Message):
    user_info = db.get_reg_data(message.from_user.id)
    if not user_info:
        await message.answer("Привет!\n"
                            "Я бот для твоих тренировок!\n"
                            "Нажми кнопку снизу для регистарции.", reply_markup=kb.register)
    else:
        name = user_info
        await message.answer(f"Привет {name}!\n"
                             "Нажимай кнопку снизу и выбирай упражнение и смотри для него правильную технику выполнения.", reply_markup=kb.main)

@router.message(F.text == "📝Начать регистрацию")
async def register_start(message: Message, state: FSMContext):
    user_info = db.get_reg_data(message.from_user.id)
    if not user_info:
        await message.answer("Как могу тебя называть?")

        await state.set_state(st.Register.waiting_name)
    else:
        name = user_info
        await message.answer(f"Привет {name}!\nНажимай кнопку снизу чтобы выбрать упражнение!")


@router.message(st.Register.waiting_name)
async def register_end(message: Message, state: FSMContext):
    text = message.text.strip()
    user_info = db.get_reg_data(message.from_user.id)
    if not user_info:
        await message.answer(f"Привет {text}!\nТы успешно зарегистрировался!", reply_markup=kb.main)
        db.register(message.from_user.id, text)
    else:
        name = user_info
        await message.answer(f"Ты уже зарегистрировался как {name}")
    await state.clear()