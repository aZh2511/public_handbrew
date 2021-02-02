from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderOut(StatesGroup):

    Order_milk = State()
    Order_more = State()
    Order_dessert = State()
    Order_dessert_taste = State()
    Order_dessert_qnt = State()
    Order_dessert_more = State()
    Order_dessert_q = State()

    Order_time = State()

    Order_finish = State()
    Order_specify = State()
