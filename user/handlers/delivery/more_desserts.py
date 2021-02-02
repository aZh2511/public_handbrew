from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import bot
from loader import dp
from user.keyboards import create_dessert_kb, kb_main_menu, kb_choose_house
from user.states import MenuClass, OrderClass


@dp.message_handler(text='Да', state=OrderClass.Order_dessert_q)
async def process_more_choice(message: Message):
    """Processes more dessert choice "Yes".
     on ending sends dessert choice keyboard (from beginning)"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите десерт:',
                           reply_markup=create_dessert_kb())
    await OrderClass.Order_dessert_taste.set()


@dp.message_handler(text='Нет', state=OrderClass.Order_dessert_q)
async def process_more_choice(message: Message):
    """Processes more dessert choice "No".
    on ending asks for house, sends appropriate keyboard"""
    await bot.send_message(chat_id=message.chat.id, text='В какой дом будем доставлять?',
                           reply_markup=kb_choose_house)
    await OrderClass.next()


@dp.message_handler(text='Заново', state=OrderClass.Order_dessert_q)
async def process_more_choice(message: Message, state: FSMContext):
    """Processes more dessert choice "Repeat".
    on ending remove current choice and starts dessert choice
    from the beginning"""
    await state.update_data(dessert_order='')
    await state.update_data(dessert_price=0)
    await OrderClass.Order_dessert_taste.set()

    await bot.send_message(chat_id=message.chat.id, text='Выберите десерт:',
                           reply_markup=create_dessert_kb())


@dp.message_handler(text='Отмена', state=OrderClass.Order_dessert_q)
async def cancel_order(message: Message, state: FSMContext):
    """Processes more drinks choice "Cancel".
     on ending sends start-menu"""
    await bot.send_message(chat_id=message.chat.id, text='Ваш заказ отменен!',
                           reply_markup=kb_main_menu)
    await state.reset_data()
    await MenuClass.Main_menu.set()


@dp.message_handler(content_types=['text'], state=OrderClass.Order_dessert_q)
async def incorrect_input(message: Message):
    """Processes incorrect more drink input"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов')
