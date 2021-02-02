from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import bot
from loader import dp
from user.keyboards import create_drinks_kb
from user.states import OrderOut, OrderClass


# TODO: straight inserting into data storage of data (without using additional variable


@dp.message_handler(text='Самовынос', state=OrderClass.Order_deliver_type)
async def choose_delivering_type(message: Message, state: FSMContext):
    """ Self-delivery. Sends keyboard of drinks choice and sets
    appropriate state"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите, что хотите заказать:'
                                                         '\nДесерты можно будет добавить в конце',
                           reply_markup=create_drinks_kb())
    await OrderOut.Order_milk.set()
    await state.update_data(price=0)
    await state.update_data(dessert_price=0)
    await state.update_data(full_drink='')
    await state.update_data(dessert_order='')
    await state.update_data(order_type='self-delivery')
