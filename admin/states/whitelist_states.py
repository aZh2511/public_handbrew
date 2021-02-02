from aiogram.dispatcher.filters.state import State, StatesGroup


class WhiteList(StatesGroup):
    GetInfo = State()
    ChangeStatus = State()
