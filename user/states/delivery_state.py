from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderClass(StatesGroup):
    Order_deliver_type = State()
    Order_milk = State()
    Order_more = State()

    Order_dessert = State()
    Order_dessert_taste = State()
    Order_dessert_qnt = State()
    Order_dessert_more = State()
    Order_dessert_q = State()

    Order_house = State()
    Order_floor = State()
    Order_entrance = State()
    Order_flat = State()
    Order_time = State()

    Order_finish = State()
    Order_specify = State()
