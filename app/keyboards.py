from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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