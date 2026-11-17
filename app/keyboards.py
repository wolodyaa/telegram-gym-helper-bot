from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


register = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📝Начать регистрацию")]],
    resize_keyboard=True,
    input_field_placeholder="Нажмите на кнопку..."
)

main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🏋️‍♂️Выбрать упражнение")],
              [KeyboardButton(text="⚙️Настройки")]],
    resize_keyboard=True, 
    input_field_placeholder="Нажмите на кнопку..."
)

confirm = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="✔️Да", callback_data="confirm_yes")],
                     [InlineKeyboardButton(text="❌Нет", callback_data="confirm_no")]]
)


returns = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="↩️Вернуться", callback_data="return")]]
)


settings = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="🗑️УДАЛИТЬ ДАННЫЕ", callback_data="delete_data")]]
)


exercises = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="💪Руки", callback_data="ex_arms")],
                     [InlineKeyboardButton(text="🦵Ноги", callback_data="ex_legs")],
                     [InlineKeyboardButton(text="🏋️Спина", callback_data="ex_back")],
                     [InlineKeyboardButton(text="🦍Грудь", callback_data="ex_boobs")]]
)