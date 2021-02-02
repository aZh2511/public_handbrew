from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from app import bot
from config import *
from database.functions import add_order
from loader import dp
from user.keyboards import kb_main_menu, kb_specify_order, kb_choose_deliver_type
from user.states import MenuClass, OrderClass


@dp.message_handler(content_types=['text'], state=OrderClass.Order_finish)
async def clarify_order(message: Message, state: FSMContext):
    """ Gets commentaries for delivery. Specifies order
    Sends the order and asks if the order is correct """
    additional_comments = message.text

    await state.update_data(additional_comments=additional_comments)
    data = await state.get_data()
    await state.update_data(total_price=(data.get('price')+data.get('dessert_price')))
    await bot.send_message(chat_id=message.chat.id,
                           text=f"""Ваш заказ:
Напитки: <b>{data.get("full_drink")}</b>
Десерты: <b>{data.get("dessert_order")}</b>
Дом: <b>{data.get("chosen_house")}</b>
Подъезд: <b>{data.get("chosen_entrance")}</b>
Этаж: <b>{data.get("floor")}</b>
Квартира: <b>{data.get("apartment_number")}</b>
Когда: <b>{data.get("chosen_time")}</b>
Примечание к заказу: <b>{data.get("additional_comments")}</b>
Цена: <b>{data.get("price")+data.get('dessert_price')}</b>""",

                           reply_markup=ReplyKeyboardRemove(),  parse_mode=ParseMode.HTML)

    await bot.send_message(chat_id=message.chat.id, text='Ваш заказ правильный?',
                           reply_markup=kb_specify_order)

    await OrderClass.next()


@dp.message_handler(text='Заново', state=OrderClass.Order_specify)
async def specify_order(message: Message, state: FSMContext):
    """ Processes specifying of order "From beginning"
     resets data and starts from beginning"""
    await state.reset_data()
    await bot.send_message(chat_id=message.chat.id, text='Выберите способ доставки:',
                           reply_markup=kb_choose_deliver_type)
    await state.reset_data()
    await state.update_data(price=20)
    await OrderClass.Order_deliver_type.set()

# Keyboard for admin chat
order_confirm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Заказ принят', callback_data='accepted')]
])


@dp.message_handler(text='Всё верно', state=OrderClass.Order_specify)
async def specify_order(message: Message, state: FSMContext):
    """Finishes order, forwards info to the admin-chat"""

    data = await state.get_data()
    add_order(message, data)
    await bot.send_message(chat_id=message.chat.id, text='Спасибо за заказ!'
                                                         '\nВаш заказ обрабатывается!',
                           reply_markup=ReplyKeyboardRemove())

    await bot.send_message(chat_id=admin_chat_id, text=f"""
Поступил заказ на доставку:
Напитки: <b>{data.get("full_drink")}</b>
Десерты: <b>{data.get("dessert_order")}</b>
Дом: <b>{data.get("chosen_house")}</b>
Подъезд: <b>{data.get("chosen_entrance")}</b>
Этаж: <b>{data.get("floor")}</b>
Квартира: <b>{data.get("apartment_number")}</b>
Когда: <b>{data.get("chosen_time")}</b>
Примечание к заказу: <b>{data.get("additional_comments")}</b>
Цена: <b>{data.get("total_price")}</b>
Ссылка на чат: <b> tg://user?id={message.from_user.id}</b>
Тег (может не быть): <b>@{message.from_user.username}</b>
Айди чата: <b>{message.chat.id}</b>
""",
                           reply_markup=order_confirm, parse_mode=ParseMode.HTML)
    await MenuClass.Main_menu.set()


@dp.message_handler(text='Отмена', state=OrderClass.Order_specify)
async def cancel_order(message: Message, state: FSMContext):
    """Processes more drinks choice "Cancel".
     on ending sends start-menu"""
    await bot.send_message(chat_id=message.chat.id, text='Ваш заказ отменен!',
                           reply_markup=kb_main_menu)
    await state.reset_data()
    await MenuClass.Main_menu.set()


@dp.message_handler(content_types=['text'], state=OrderClass.Order_specify)
async def incorrect_input(message: Message):
    """Processes incorrect input"""

    await bot.send_message(chat_id=message.chat.id, text='Выберите, пожалуйста, из предложенных вариантов')
