from aiogram.types import Message

from admin.states import AdminPanel
from app import bot
from loader import dp
from admin.functions import change_availability
from ..keyboards import *


@dp.message_handler(text='Десерты', state=AdminPanel.Category_choose)
async def set_availability(message: Message):
    """ Desserts availability """
    await bot.send_message(chat_id=message.chat.id, text='Выберите, что есть в наличии',
                           reply_markup=admin_dessert_kb())
    await AdminPanel.AvailabilitySweets.set()


@dp.message_handler(text='Назад', state=AdminPanel.AvailabilitySweets)
async def sweets_availability(message: Message):
    """ Back to main menu of admin panel """
    await bot.send_message(chat_id=message.chat.id, text='Выберите категорию:',
                           reply_markup=kb_availability_choose)
    await AdminPanel.Category_choose.set()


@dp.message_handler(content_types=['text'], state=AdminPanel.AvailabilitySweets)
async def sweets_availability(message: Message):
    """ Changes dessert availability """
    text = change_availability(message)
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=admin_dessert_kb())
