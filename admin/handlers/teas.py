from aiogram.types import Message

from admin.functions import change_availability
from admin.states import AdminPanel
from app import bot
from loader import dp
from ..keyboards import *


@dp.message_handler(text='Чаи', state=AdminPanel.Category_choose)
async def set_availability(message: Message):
    """ Tea availability """
    await bot.send_message(chat_id=message.chat.id, text='Выберите, что есть в наличии',
                           reply_markup=admin_tea_kb())
    await AdminPanel.AvailabilityTea.set()


@dp.message_handler(text='Назад', state=AdminPanel.AvailabilityTea)
async def tea_availability(message: Message):
    """ Back to main menu of admin panel """
    await bot.send_message(chat_id=message.chat.id, text='Выберите категорию:',
                           reply_markup=kb_availability_choose)
    await AdminPanel.Category_choose.set()


@dp.message_handler(content_types=['text'], state=AdminPanel.AvailabilityTea)
async def tea_availability(message: Message):
    """ Changes tea availability """
    text = change_availability(message)
    await bot.send_message(chat_id=message.chat.id, text=text,
                           reply_markup=admin_tea_kb())
