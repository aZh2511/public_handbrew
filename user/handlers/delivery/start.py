from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from app import bot
from loader import dp
from user.keyboards import create_drinks_kb
from user.states import OrderClass


# TODO: remove pillow


@dp.message_handler(text='Доставка', state=OrderClass.Order_deliver_type)
async def choose_delivering_type(message: Message, state: FSMContext):
    """ Delivery. Sends keyboard of drinks choice and sets
    appropriate state """
    await bot.send_message(chat_id=message.chat.id, text='Выберите, что хотите заказать:\n'
                                                         '<i>Десерты можно будет добавить после выбора напитка</i>\n'
                                                         '❗Оплата при получении картой или наличными'
                                                         '\n<b>Стоимость доставки - 20 грн</b>',
                           reply_markup=create_drinks_kb(), parse_mode=ParseMode.HTML)
    await OrderClass.next()
    await state.update_data(price=20)
    await state.update_data(dessert_price=0)
    await state.update_data(full_drink='')
    await state.update_data(dessert_order='')
    await state.update_data(order_type='delivery')
