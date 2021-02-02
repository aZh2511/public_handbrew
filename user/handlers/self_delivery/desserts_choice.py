from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import bot
from aiogram.dispatcher.filters import Text
from config import *
from loader import dp
from user.handlers.calculate_price import calculate_price
from user.keyboards import create_macaroon_kb, create_brownie_kb, kb_additional_comments, kb_order_more, \
    kb_choose_qnt_dessert, create_dessert_kb
from user.states import OrderOut
from database.functions.db_positions_lists import dessert_menu, brownies_menu, macaroons_menu


@dp.message_handler(text='Макаруны (40 грн)', state=OrderOut.Order_dessert_taste)
async def macaroon_taste(message: Message, state: FSMContext):
    await state.update_data(dessert_taste=message.text)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=MACAROON_PHOTO)
    await bot.send_message(chat_id=message.chat.id, text='Выберите вкус пожалуйста:',
                           reply_markup=create_macaroon_kb())
    await OrderOut.next()


@dp.message_handler(text='Брауни (55 грн)', state=OrderOut.Order_dessert_taste)
async def brownie_taste(message: Message, state: FSMContext):
    await state.update_data(dessert_taste=message.text)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=BROWNIE_PHOTO)
    await bot.send_message(chat_id=message.chat.id, text='Выберите вкус пожалуйста:',
                           reply_markup=create_brownie_kb())
    await OrderOut.next()


@dp.message_handler(text='Не нужно', state=OrderOut.Order_dessert_taste)
async def dessert_qnt(message: Message, state: FSMContext):
    """Processes dessert choice "No need".
    on ending moves to making commentaries for delivery"""
    await bot.send_message(chat_id=message.chat.id, text="""
Ваши примечания к заказу?
Например:
<b>Доставить на этаж.
На Ристретто
Если примечаний нет, то нажмите "Нет"</b>
""",
                           reply_markup=kb_additional_comments)
    await state.update_data(dessert='Не нужно')
    await OrderOut.Order_time.set()


@dp.message_handler(Text(equals=dessert_menu()), state=OrderOut.Order_dessert_taste)
async def dessert_qnt(message: Message, state: FSMContext):
    """Gets dessert choice for no-taste positions. Asks quantity """

    chosen_dessert = message.text
    await state.update_data(dessert=chosen_dessert)
    await bot.send_message(chat_id=message.chat.id, text='Укажите количество (штук), пожалуйста'
                                                         '\nИли напишите вручную',
                           reply_markup=kb_choose_qnt_dessert)
    await OrderOut.Order_dessert_more.set()


@dp.message_handler(content_types=['text'], state=OrderOut.Order_dessert_taste)
async def dessert_qnt(message: Message):
    """Processes incorrect input"""

    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов',
                           reply_markup=create_dessert_kb())


@dp.message_handler(Text(equals=(macaroons_menu())), state=OrderOut.Order_dessert_qnt)
async def dessert_qnt(message: Message, state: FSMContext):
    """Gets dessert choice. Asks quantity """
    data = await state.get_data()
    chosen_dessert = f'{data.get("dessert_taste")} {message.text}'
    await state.update_data(dessert=chosen_dessert)
    await bot.send_message(chat_id=message.chat.id, text='Укажите количество, пожалуйста (штук).'
                                                         '\nИли напишите вручню',
                           reply_markup=kb_choose_qnt_dessert)
    await OrderOut.next()


@dp.message_handler(Text(equals=(brownies_menu())), state=OrderOut.Order_dessert_qnt)
async def dessert_qnt(message: Message, state: FSMContext):
    """Gets dessert choice. Asks quantity """
    data = await state.get_data()
    chosen_dessert = f'{data.get("dessert_taste")} {message.text}'
    await state.update_data(dessert=chosen_dessert)
    await bot.send_message(chat_id=message.chat.id, text='Укажите количество, пожалуйста (штук).'
                                                         '\nИли напишите вручню',
                           reply_markup=kb_choose_qnt_dessert)
    await OrderOut.next()


@dp.message_handler(content_types=['text'], state=OrderOut.Order_dessert_qnt)
async def incorrect_input(message: Message):
    """Processes incorrect dessert input"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов')


@dp.message_handler(lambda message: str(message.text).isdigit(), state=OrderOut.Order_dessert_more)
async def order_more_desserts(message: Message, state: FSMContext):
    """ Gets quantity of chosen dessert. Calculates price.
    On ending asks for more desserts, sends appropriate keyboard """
    chosen_dessert_qnt = message.text
    await state.update_data(dessert_qnt=chosen_dessert_qnt)
    data = await state.get_data()
    current_dessert_order = data.get("dessert_order")
    await state.update_data(dessert_order=f'{current_dessert_order}\n'
                                          f'{data.get("dessert")} {message.text} шт\n')
    current_price = int(data.get("dessert_price")) + int(calculate_price(data.get("dessert")) * int(message.text))
    await state.update_data(dessert_price=current_price)

    await bot.send_message(chat_id=message.chat.id, text='Ещё десерты?',
                           reply_markup=kb_order_more)
    await OrderOut.next()


@dp.message_handler(content_types=['text'], state=OrderOut.Order_dessert_more)
async def incorrect_input(message: Message):
    """Processes incorrect qnt input"""
    await bot.send_message(chat_id=message.chat.id, text='Укажите количество цифрой, пожалуйста!',
                           reply_markup=kb_choose_qnt_dessert)
