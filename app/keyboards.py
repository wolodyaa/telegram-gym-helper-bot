from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

register = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📝Начать регистрацию")]],
    resize_keyboard=True,
    input_field_placeholder="Нажмите на кнопку..."
)

main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🏋️‍♂️Выбрать упражнение")]],
    resize_keyboard=True, 
    input_field_placeholder="Нажмите на кнопку..."
)

confirm = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data="confirm_yes")],
                     [InlineKeyboardButton(text="Нет", callback_data="confirm_no")]]
)