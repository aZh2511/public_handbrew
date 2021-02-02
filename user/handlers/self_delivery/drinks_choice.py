from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from app import bot
from database.functions.db_positions_lists import drinks_menu, milks_menu, tea_menu, fruit_tea_menu
from loader import dp
from user.handlers.calculate_price import calculate_price
from user.keyboards import create_tea_kb, create_fruit_tea_kb, create_drinks_kb, kb_order_more, create_milk_kb
from user.states import OrderOut


@dp.message_handler(text='Чай (330 мл) 27 грн', state=OrderOut.Order_milk)
async def choose_full_drink(message: Message, state: FSMContext):
    """ Processes simple tea. On ending sends taste-choice keyboard"""
    chosen_drink = f'{message.text}'
    data = await state.get_data()
    await state.update_data(drink=chosen_drink)
    current_price = int(data.get("price")) + int(calculate_price(message))
    await state.update_data(price=current_price)

    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста:',
                           reply_markup=create_tea_kb())
    await OrderOut.next()


@dp.message_handler(text='Фруктовый Чай (330 мл) 37 грн', state=OrderOut.Order_milk)
async def choose_full_drink(message: Message, state: FSMContext):
    """ Processes simple tea. On ending sends taste-choice keyboard"""
    if not create_fruit_tea_kb().values['keyboard']:
        await bot.send_message(chat_id=message.chat.id, text='Фруктового чая, к сожалению, нет в наличии'
                                                             '\nВыберите, что хотите заказать:',
                               reply_markup=create_drinks_kb())
        await OrderOut.Order_milk.set()
    else:
        chosen_drink = f'{message.text}'
        data = await state.get_data()
        current_price = int(data.get("price")) + int(calculate_price(message))
        await state.update_data(price=current_price)
        await state.update_data(drink=chosen_drink)

        await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста:',
                               reply_markup=create_fruit_tea_kb())
        await OrderOut.next()


@dp.message_handler(Text(equals=['Еспресо (30 мл) 27 грн', 'Американо (130 мл) 27 грн', 'Допио (60 мл) 35 грн',
                                 'Фильтр Маленький (170 мл) 30 грн', 'Фильтр Большой (330 мл) 40 грн']),
                    state=OrderOut.Order_milk)
async def choose_full_drink(message: Message, state: FSMContext):
    """ Processes no-milk coffee drinks. On ending sends one-more drink choice"""
    chosen_drink = f'{message.text}'
    data = await state.get_data()
    current_price = int(data.get("price")) + int(calculate_price(message))
    await state.update_data(price=current_price)
    current_order = f'{data.get("full_drink")}\n{chosen_drink}'

    await state.update_data(full_drink=current_order)

    await bot.send_message(chat_id=message.chat.id, text='Ещё напитки?',
                           reply_markup=kb_order_more)

    await OrderOut.Order_dessert.set()


@dp.message_handler(Text(equals=drinks_menu()), state=OrderOut.Order_milk)
async def choose_full_drink(message: Message, state: FSMContext):
    """ Processes other coffee drinks, on ending sends milk-choice keyboard"""

    chosen_drink = f'{message.text}'
    data = await state.get_data()

    current_price = int(data.get("price")) + int(calculate_price(message))
    await state.update_data(price=current_price)
    await state.update_data(drink=chosen_drink)
    await bot.send_message(chat_id=message.chat.id, text='На каком молоке?',
                           reply_markup=create_milk_kb())
    await OrderOut.next()


@dp.message_handler(content_types=['text'], state=OrderOut.Order_milk)
async def incorrect_input(message: Message):
    """Processes incorrect drink input"""

    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов',
                           reply_markup=create_drinks_kb())


@dp.message_handler(Text(equals=milks_menu()), state=OrderOut.Order_more)
async def process_drink_order(message: Message, state: FSMContext):
    """Processes milk choice. Calculates price. On ending sends more-drinks-choice keyboard"""
    chosen_milk = message.text
    data = await state.get_data()

    await state.update_data(milk=chosen_milk)

    # Дринк ордер
    full_drink = f'{data.get("full_drink")}\n{data.get("drink")} {message.text}\n'
    await state.update_data(full_drink=full_drink)
    current_price = int(data.get("price")) + int(calculate_price(message))
    await state.update_data(price=current_price)
    await bot.send_message(chat_id=message.chat.id, text='Ещё напитки?',
                           reply_markup=kb_order_more)
    await OrderOut.next()


@dp.message_handler(Text(equals=tea_menu()), state=OrderOut.Order_more)
async def process_drink_order(message: Message, state: FSMContext):
    """Processes milk choice. Calculates price. On ending sends more-drinks-choice keyboard"""
    chosen_milk = message.text
    data = await state.get_data()

    await state.update_data(milk=chosen_milk)

    # Дринк ордер
    full_drink = f'{data.get("full_drink")}\n{data.get("drink")} {message.text}\n'
    await state.update_data(full_drink=full_drink)
    current_price = int(data.get("price")) + int(calculate_price(message))
    await state.update_data(price=current_price)
    await bot.send_message(chat_id=message.chat.id, text='Ещё напитки?',
                           reply_markup=kb_order_more)
    await OrderOut.next()


@dp.message_handler(Text(equals=fruit_tea_menu()), state=OrderOut.Order_more)
async def process_drink_order(message: Message, state: FSMContext):
    """Processes milk choice. Calculates price. On ending sends more-drinks-choice keyboard"""
    chosen_milk = message.text
    data = await state.get_data()

    await state.update_data(milk=chosen_milk)

    # Дринк ордер
    full_drink = f'{data.get("full_drink")}\n{data.get("drink")} {message.text}\n'
    await state.update_data(full_drink=full_drink)
    current_price = int(data.get("price")) + int(calculate_price(message))
    await state.update_data(price=current_price)
    await bot.send_message(chat_id=message.chat.id, text='Ещё напитки?',
                           reply_markup=kb_order_more)
    await OrderOut.next()


@dp.message_handler(content_types=['text'], state=OrderOut.Order_more)
async def incorrect_input(message: Message):
    """Processes incorrect milk input"""

    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов')
