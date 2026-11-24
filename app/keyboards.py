from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database import get_usernames, get_data

register = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="📝Начать регистрацию")]], resize_keyboard=True, input_field_placeholder="Начните регистрацию...")


admin_panel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="👀Посмотреть данные", callback_data="check_data")],
                                                    [InlineKeyboardButton(text="✍️Редактировать данные", callback_data="edit_data")],
                                                    [InlineKeyboardButton(text="🗑Удалить данные", callback_data="delete_data")],
                                                    [InlineKeyboardButton(text="◀️Выйти из панели", callback_data="admin_leave")]])


return_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️Вернуться", callback_data="return")]])


confirm_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data="confirm_yes"), InlineKeyboardButton(text="Нет", callback_data="confirm_no")]])


async def users(prefix):
    users = get_usernames()
    keyboard = InlineKeyboardBuilder()
    for user in users:
        username = user[0]
        if not username:
            continue
        keyboard.add(InlineKeyboardButton(text=username, callback_data=f"{prefix}_user_{username}"))
    keyboard.row()
    keyboard.add(InlineKeyboardButton(text="◀️Вернуться", callback_data="return"))
    return keyboard.adjust(2).as_markup()


async def edit_user(username):
    user_data = get_data(username)

    if not user_data:
        return None

    user_id, name, surname = user_data

    editable_fields = [
        ("name", "Имя", name),
        ("surname", "Фамилия", surname)
    ]

    keyboard = InlineKeyboardBuilder()

    for field_key, field_name, field_value in editable_fields:

        keyboard.add(InlineKeyboardButton(text=f'{field_name}: {field_value}',
                                           callback_data=f"edit_field_{field_key}_{username}"
        ))

    keyboard.row()
    keyboard.add(InlineKeyboardButton(text="◀️Вернуться", callback_data="return"))

    return keyboard.adjust(1).as_markup()