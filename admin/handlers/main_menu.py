from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from admin.states import AdminPanel, WhiteList
from app import bot
from config import IP_WHITELIST
from database.functions import black_list
from loader import dp
from ..keyboards import *


@dp.message_handler(Command(['admin']), lambda message: message.from_user.id in IP_WHITELIST, state='*')
async def admin_panel(message: Message):
    """Admin panel"""
    if message.from_user.id in IP_WHITELIST:
        await bot.send_message(chat_id=message.chat.id, text='Админ панель',
                               reply_markup=kb_admin_panel)
        await AdminPanel.MainMenu.set()


@dp.message_handler(text=['Вайтлист'], state=AdminPanel.MainMenu)
async def get_user_status(message: Message):
    """ Asks user id for making db request """
    text = black_list()
    await bot.send_message(chat_id=message.chat.id, text=
    f"""
Заблокированные пользователи:

{text}

Отправьте мне айди пользователя, которого нужно 
проверить.""",
                           reply_markup=ReplyKeyboardRemove())
    await WhiteList.GetInfo.set()


@dp.message_handler(text='Наличие', state=AdminPanel.MainMenu)
async def choose_type(message: Message):
    """ Chooses category for changing availability """
    await bot.send_message(chat_id=message.chat.id, text='Выберите:',
                           reply_markup=kb_availability_choose)
    await AdminPanel.next()
