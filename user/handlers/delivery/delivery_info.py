import datetime
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode
from aiogram.types import ReplyKeyboardRemove

from app import bot
from loader import dp
from user.keyboards import kb_choose_time, kb_choose_entrance, kb_additional_comments
from user.states import OrderClass


@dp.message_handler(Text(equals=['Драгоманова 2', 'Драгоманова 2А',
                                 'Драгоманова 2Б', 'Драгоманова 4А',
                                 'Пчелки 8']), state=OrderClass.Order_house)
async def choose_entrance(message: Message, state: FSMContext):
    """Gets house, asks for entrance"""
    chosen_house = message.text
    await state.update_data(chosen_house=chosen_house)
    await bot.send_message(chat_id=message.chat.id, text='Замечательно, какой подъезд?',
                           reply_markup=kb_choose_entrance)
    await OrderClass.next()


@dp.message_handler(content_types=['text'], state=OrderClass.Order_house)
async def incorrect_input(message: Message):
    """Processes incorrect input"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов')


@dp.message_handler(Text(equals=['Первый', 'Второй', 'Третий']), state=OrderClass.Order_floor)
async def choose_apartment_number(message: Message, state: FSMContext):
    """Gets entrance asks for floor """
    chosen_entrance = message.text
    await bot.send_message(chat_id=message.chat.id, text='Какой Этаж?\nНапишите, пожалуйста, цифрой',
                           reply_markup=ReplyKeyboardRemove())
    await state.update_data(chosen_entrance=chosen_entrance)
    await OrderClass.next()


@dp.message_handler(content_types=['text'], state=OrderClass.Order_floor)
async def incorrect_input(message: Message):
    """Processes incorrect input"""
    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов',
                           reply_markup=kb_choose_entrance)


@dp.message_handler(lambda message: str(message.text).isdigit(), state=OrderClass.Order_entrance)
async def choose_apartment_number(message: Message, state: FSMContext):
    """ Gets floor asks for apartment number """
    # TODO: обработка ввода, чтоб получал только int (digit). попробовать через while
    chosen_floor = message.text
    await state.update_data(floor=chosen_floor)
    await bot.send_message(chat_id=message.chat.id, text='Замечательно, какая квартира?'
                                                         '\nНапишите номер квартиры цифрой',
                           reply_markup=ReplyKeyboardRemove())
    await OrderClass.next()


@dp.message_handler(content_types=['text'], state=OrderClass.Order_entrance)
async def choose_apartment_number(message: Message):
    """Processes incorrect floor input"""
    await bot.send_message(chat_id=message.chat.id, text='Введите этаж цифрой, пожалуйста!')


@dp.message_handler(lambda message: str(message.text).isdigit(), state=OrderClass.Order_flat)
async def choose_time(message: Message, state: FSMContext):
    """Gets apartment number. Asks for time-delivery"""
    apartment_number = message.text
    await state.update_data(apartment_number=apartment_number)
    now = datetime.datetime.now().strftime('%H:%M')
    await bot.send_message(chat_id=message.chat.id, text=f'Через сколько вам доставить ваш заказ?\n'
                                                         f'Время сейчас: {now}',
                           reply_markup=kb_choose_time)
    await OrderClass.next()


@dp.message_handler(content_types=['text'], state=OrderClass.Order_flat)
async def choose_apartment_number(message: Message):
    """Processes incorrect floor input"""
    await bot.send_message(chat_id=message.chat.id, text='Введите номер квартиры цифрой, пожалуйста!')


@dp.message_handler(Text(equals=['Через 10 минут', 'Через 15 мин',
                                 'Через 20 минут', 'Через 25 мин']), state=OrderClass.Order_time)
async def choose_desserts(message: Message, state: FSMContext):
    """Gets delivery_time. Asks for commentaries for order """
    chosen_time = message.text
    await state.update_data(chosen_time=chosen_time)

    await bot.send_message(chat_id=message.chat.id, text="""
Ваши примечания к заказу?
Например:
<b>Доставить на этаж.
На Ристретто
Если примечаний нет, то нажмите "Нет"</b>
    """,
                           reply_markup=kb_additional_comments, parse_mode=ParseMode.HTML)
    await OrderClass.next()


@dp.message_handler(content_types=['text'], state=OrderClass.Order_time)
async def incorrect_input(message: Message):
    """ Processes incorrect input """

    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов')
