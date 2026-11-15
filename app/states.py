from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
    waiting_name = State()
    waiting_surname = State()
    waiting_group = State()
    waiting_confirm = State()