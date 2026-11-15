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
        await message.answer("Введи своё полное имя.")

        await state.set_state(st.Register.waiting_name)
    else:
        name = user_info
        await message.answer(f"Ты уже зарегистрировался как: {name}!\nТак что нажимай кнопку снизу чтобы выбрать упражнение!")


@router.message(st.Register.waiting_name)
async def register_name(message: Message, state: FSMContext):
    text = message.text.strip()
    await state.update_data(name=text)

    await message.answer("Введи свою фамилию.")

    await state.set_state(st.Register.waiting_surname)


@router.message(st.Register.waiting_surname)
async def register_surname(message: Message, state: FSMContext):
    text = message.text.strip()
    await state.update_data(surname=text)

    await message.answer("Введи свою группу.")

    await state.set_state(st.Register.waiting_group)


@router.message(st.Register.waiting_group)
async def register_end(message: Message, state: FSMContext):
    text = message.text.strip()
    await state.update_data(group=text)
    data = await state.get_data()

    await message.answer("Твое данные:\n"
                         f"Имя: {data["name"]}.\n"
                         f"Фамилия: {data["surname"]}.\n"
                         f"Группа: {data["group"]}.\n"
                         "Все данные указаны верно?",
                           reply_markup=kb.confirm)
    await state.set_state(st.Register.waiting_confirm)


@router.callback_query(st.Register.waiting_confirm, F.data == "confirm_yes")
async def confirm_yes(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.edit_text("Твое данные cохранены как:\n"
                             f"Имя: {data["name"]}.\n"
                             f"Фамилия: {data["surname"]}.\n"
                             f"Группа: {data["group"]}.\n"
    )

    await callback.message.answer("Теперь ты можешь нажать кнопку снизу и выбрать упражнение",
                                   reply_markup=kb.main)
    
    db.register(callback.from_user.id, data["name"], data["surname"], data["group"])
    await callback.answer()
    await state.clear()


@router.callback_query(st.Register.waiting_confirm, F.data == "confirm_no")
async def confirm_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Хорошо. Начнем регистрацию заново.")


    await callback.message.answer("Введите своё имя.")
    await callback.answer()
    await state.set_state(st.Register.waiting_name)