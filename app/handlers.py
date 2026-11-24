import re

from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from assets.config import ADMIN_ID

import app.keyboards as kb
import app.states as st
import app.database as db


router = Router()

@router.message(CommandStart())
async def cmdstart(message: Message):
    user_info = db.get_reg_data(message.from_user.id)
    if not user_info:
        await message.answer("Привет! Нажимай кнопку снизу чтобы начать регистрацию.", reply_markup=kb.register)
    else:
        name = user_info
        await message.answer(f"Привет {name}!")


@router.message(F.text == "📝Начать регистрацию")
async def register_start(message: Message, state: FSMContext):
    user_info = db.get_reg_data(message.from_user.id)
    if not user_info:
        await message.answer("Введи своё имя.")
        await state.set_state(st.Register.waiting_name)
    else:
        name = user_info
        await message.answer(f"Ты уже зарегистрировался как: {name}.")


@router.message(st.Register.waiting_name)
async def register_name(message: Message, state: FSMContext):
    name = message.text.strip()
    await message.answer("Введи свою фамилию.")
    await state.update_data(name=name)
    await state.set_state(st.Register.waiting_surname)


@router.message(st.Register.waiting_surname)
async def register_surname(message: Message, state: FSMContext):
    surname = message.text.strip()
    await message.answer("Введи свой уникальный идентификатор пользователя на латинице.(НЕЛЬЗЯ ИЗМЕНИТЬ)")
    await state.update_data(surname=surname)
    await state.set_state(st.Register.waiting_username)


@router.message(st.Register.waiting_username)
async def register_username(message: Message, state: FSMContext):
    username = message.text.strip()
    data = await state.get_data()

    if re.fullmatch(r"[A-Za-z]+", username):
        if db.check_username_exists(username):
            await message.answer("Твой идентификатор уже занят. Придумай другой.")
            return
        else:

            await message.answer("Ты успешно зарегистрировался!\n"
                                "Твои данные:\n"
                                f"Имя: {data['name']}\n"
                                f"Фамилия: {data['surname']}\n"
                                f"Уникальный идентификатор: {username}")
            db.register(message.from_user.id, username, data['name'], data['surname'])
            await state.clear()

    else:
        await message.answer("Идентификатор должен быть только из латинский букв.\n"
                             "Введите свой уникальный идентификатор пользователя на латинице.(НЕЛЬЗЯ ИЗМЕНИТЬ)")
        return



@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Вы вошли в панель администратора.", reply_markup=kb.admin_panel)
    else:
        await message.answer("🚫")


@router.callback_query(F.data == "check_data")
async def admin_check_data(callback: CallbackQuery):
    users = db.get_usernames()
    if not users:
        await callback.message.edit_text("Нет пользователей для просмотра.", reply_markup=kb.return_button)
    else:
        await callback.message.edit_text("Выберите пользователя.", reply_markup= await kb.users("check"))
        await callback.answer()


@router.callback_query(F.data == "delete_data")
async def admin_delete_data(callback: CallbackQuery):
    users = db.get_usernames()
    if not users:
        await callback.message.edit_text("Нет пользователей для удаления.", reply_markup=kb.return_button)
    else:
        await callback.message.edit_text("Выберите пользователя.", reply_markup= await kb.users("delete"))
        await callback.answer()


@router.callback_query(F.data == "admin_leave")
async def admin_leave(callback: CallbackQuery):
    await callback.message.edit_text("Вы вышли из панели администратора.")


@router.callback_query(F.data.startswith("check_user_"))
async def admin_show_data(callback: CallbackQuery):
    username = callback.data.replace("check_user_", "")
    user_data = db.get_data(username)
    if not user_data:
        await callback.message.edit_text("По данному пользователю нету данных.", reply_markup=kb.return_button)
    else:
        user_id, name, surname = user_data
        await callback.message.edit_text("Данные пользователя:\n"
                                            f"ID пользователя: {user_id}\n"
                                            f"Имя: {name}\n"
                                            f"Фамилия: {surname}\n", reply_markup=kb.return_button)
    await callback.answer()


@router.callback_query(F.data.startswith("delete_user_"))
async def admin_delete_user_data(callback: CallbackQuery, state: FSMContext):
    username = callback.data.replace("delete_user_", "")
    user_data = db.get_data(username)
    if not user_data:
        await callback.message.edit_text("У данного пользователя нету данных для удаления.", reply_markup=kb.return_button)
    else:
        user_id, name, surname = user_data
        await callback.message.edit_text("Данные пользователя:\n"
                                    f"ID пользователя: {user_id}\n"
                                    f"Имя: {name}\n"
                                    f"Фамилия: {surname}\n"
                                    "Вы действительно хотите удалить данные?", reply_markup=kb.confirm_button)
        await state.set_state(st.Confirm_Delete.waiting_confirm)
        await state.update_data(username=username)
    await callback.answer()
        

@router.callback_query(F.data == "edit_data")
async def admin_edit_data(callback: CallbackQuery):
    await callback.message.edit_text("Выберите пользователя для изменения данных.", reply_markup= await kb.users("edit"))
    await callback.answer()


@router.callback_query(F.data.startswith("edit_user_"))
async def admin_show_editable_data(callback: CallbackQuery):
    username = callback.data.replace("edit_user_", "")
    await callback.message.edit_text("Выберите данные для изменения.", reply_markup= await kb.edit_user(username))
    await callback.answer()


@router.callback_query(F.data.startswith("edit_field_"))
async def admin_edit_user_data(callback: CallbackQuery, state: FSMContext):

    data_parts = callback.data.replace("edit_field_", "").split("_", 1)

    field_to_edit = data_parts[0]
    username = data_parts[1]
    if field_to_edit == "name":
        value = "имя"
    elif field_to_edit == "surname":
        value = "фамилия"


    await state.update_data(field=field_to_edit, username=username)

    await callback.message.edit_text(f"Введите новое значение для переменной '{value}' (для @{username}).")

    await state.set_state(st.Edit_Data.waiting_new_value)
    await callback.answer()


@router.message(st.Edit_Data.waiting_new_value)
async def admin_update_new_data(message: Message, state: FSMContext):
    new_value = message.text.strip()
    data = await state.get_data()

    db.update_data(data['username'], data['field'], new_value)

    await message.answer(f"Данные обновлены! Новое значение '{new_value}' (для @{data['username']})", reply_markup=kb.admin_panel)
    await state.clear()


@router.callback_query(st.Confirm_Delete.waiting_confirm, F.data == "confirm_yes")
async def delete_confirm_yes(callback: CallbackQuery, state: FSMContext):
    username = await state.get_data()
    db.delete_data(username["username"])
    await callback.message.edit_text("Данные пользователя удалены.", reply_markup=kb.admin_panel)
    await callback.answer()
    await state.clear()


@router.callback_query(st.Confirm_Delete.waiting_confirm, F.data == "confirm_no")
async def delete_confirm_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Хорошо. Возвращаемся обратно в панель", reply_markup=kb.admin_panel)
    await callback.answer()
    await state.clear()


@router.callback_query(F.data == "return")
async def admin_return_to_users(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text("Вы вернулись в панель администратора.", reply_markup= kb.admin_panel)
    await callback.answer()