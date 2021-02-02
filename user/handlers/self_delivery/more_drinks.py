from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import bot
from loader import dp
from user.keyboards import create_drinks_kb, create_dessert_kb, kb_main_menu, kb_order_more
from user.states import OrderOut, MenuClass


@dp.message_handler(text='Да', state=OrderOut.Order_dessert)
async def process_more_choice(message: Message):
    """Processes more drinks choice "Yes".
     on ending sends drink choice keyboard (from beginning)"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите напиток?',
                           reply_markup=create_drinks_kb())
    await OrderOut.Order_milk.set()


@dp.message_handler(text='Нет', state=OrderOut.Order_dessert)
async def process_more_choice(message: Message):
    """Processes more drink choice "No".
    on ending sends desserts-choice-keyboard"""
    await bot.send_message(chat_id=message.chat.id, text='Что-нибудь из десертов?',
                           reply_markup=create_dessert_kb())
    await OrderOut.next()


@dp.message_handler(text='Заново', state=OrderOut.Order_dessert)
async def process_more_choice(message: Message, state: FSMContext):
    """Processes more drink choice "Repeat".
    on ending remove current choice and starts drink choice
    from the beginning"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите, что хотите заказать:',
                           reply_markup=create_drinks_kb())
    await OrderOut.Order_milk.set()
    await state.reset_data()
    await state.update_data(price=0)
    await state.update_data(dessert_price=0)
    await state.update_data(full_drink='')
    await state.update_data(dessert_order='')
    await state.update_data(order_type='self-delivery')


@dp.message_handler(text='Отмена', state=OrderOut.Order_dessert)
async def cancel_order(message: Message, state: FSMContext):
    """Processes more drinks choice "Cancel".
     on ending sends start-menu"""
    await bot.send_message(chat_id=message.chat.id, text='Ваш заказ отменен!',
                           reply_markup=kb_main_menu)
    await state.reset_data()
    await MenuClass.Main_menu.set()


@dp.message_handler(content_types=['text'], state=OrderOut.Order_dessert)
async def incorrect_input(message: Message):
    """Processes incorrect more drink input"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов')
