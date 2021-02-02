from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton

from app import bot
from loader import dp

order_confirm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Заказ принят', callback_data='accepted')]
])

order_deliver = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Заказ доставляется', callback_data='delivering')]
])

order_deliver_out = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Заказ готов', callback_data='ready_out')]
])

order_delivering_status = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Заказ доставлен?', callback_data='delivered')]
])


#
@dp.callback_query_handler(lambda c: c.data == 'accepted', state='*')
async def order_accepted(call: CallbackQuery, state: FSMContext):
    """ Notify user that delivery-order is accepted """
    origin_msg = str(call.message.text)
    user_id = origin_msg.split()[-1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'{call.message.text}\n\nЗаказ Принят!',
                                reply_markup=order_deliver)
    await bot.send_message(chat_id=user_id, text='Ваш заказ принят!'
                                                 '\nОжидайте уведомления о доставке!')


@dp.callback_query_handler(lambda c: c.data == 'accepted_out', state='*')
async def order_accepted(call: CallbackQuery, state: FSMContext):
    """ Notify user that self-order is accepted """
    origin_msg = str(call.message.text)
    user_id = origin_msg.split()[-1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'{call.message.text}\n\nЗаказ Принят!',
                                reply_markup=order_deliver_out)
    await bot.send_message(chat_id=user_id, text='Ваш заказ принят!'
                                                 '\nОжидайте уведомления о готовности!')


@dp.callback_query_handler(lambda c: c.data == 'ready_out', state='*')
async def order_delivering(call: CallbackQuery, state: FSMContext):
    """Notify user that self-delivery order is ready"""
    origin_msg = str(call.message.text).replace('\n\nЗаказ Принят!', '')
    user_id = origin_msg.split()[-1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'{origin_msg}\n\nЗаказ выполнен!')
    await bot.send_message(chat_id=user_id, text='Ваш заказ готов!')


@dp.callback_query_handler(lambda c: c.data == 'delivering', state='*')
async def order_delivering(call: CallbackQuery, state: FSMContext):
    """ Notify user that delivery order is being delivered """
    origin_msg = str(call.message.text).replace('\n\nЗаказ Принят!', '')
    user_id = origin_msg.split()[-1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'{origin_msg}\n\nЗаказ Доставляется!',
                                reply_markup=order_delivering_status)
    await bot.send_message(chat_id=user_id, text='Ваш заказ доставляется!')


@dp.callback_query_handler(lambda c: c.data == 'delivered', state='*')
async def order_delivered(call: CallbackQuery, state: FSMContext):
    """ Admin notification that order was delivered """
    origin_msg = str(call.message.text).replace('\n\nЗаказ Доставляется!', '')
    user_id = origin_msg.split()[-1]
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'{origin_msg}\n\nЗаказ Доставлен!')
