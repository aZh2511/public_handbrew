from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminPanel(StatesGroup):
    MainMenu = State()
    Category_choose = State()
    AvailabilityMenu = State()
    AvailabilityTea = State()
    AvailabilitySweets = State()
    AvailabilityMacaroons = State()
    AvailabilityBrownie = State()
