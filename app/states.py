from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
    waiting_name = State()
    waiting_surname = State()
    waiting_username = State()

class Confirm_Delete(StatesGroup):
    waiting_confirm = State()

class Edit_Data(StatesGroup):
    waiting_new_value = State()