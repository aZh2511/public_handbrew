from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from admin.states import WhiteList
from app import bot
from database.functions import user_get_status, user_change_status
from loader import dp
from ..keyboards import *


@dp.message_handler(lambda message: str(message.text).isdigit(), state=WhiteList.GetInfo)
async def change_user_status(message: Message, state: FSMContext):
    """ Gets user status. Asks for action (block/unblock) """
    await bot.send_message(chat_id=message.chat.id, text=f'Данный пользователь {user_get_status(message)}',
                           reply_markup=kb_whitelist)
    await state.update_data(user_id=message.text)
    await WhiteList.next()


@dp.message_handler(text=['Заблокировать / Разблокировать'], state=WhiteList.ChangeStatus)
async def change_user_status(message: Message, state: FSMContext):
    """ Changes user status black/white-list """
    data = await state.get_data()
    text = user_change_status(data.get("user_id"))
    await bot.send_message(chat_id=message.chat.id, text=f'Пользователь был {text}')
    await bot.send_message(chat_id=data.get('user_id'), text=f'Вы были {text}ы. '
                                                             f'Если произошла ошибка,'
                                                             f' обратитесь к администратору!',
                           reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text=['Назад'], state=WhiteList.ChangeStatus)
async def change_user_status(message: Message, state: FSMContext):
    """ Changes user status black/white-list """
    data = await state.get_data()
    text = user_change_status(data.get("user_id"))
    await bot.send_message(chat_id=message.chat.id, text=f'Пользователь был {text}')
    await bot.send_message(chat_id=data.get('user_id'), text=f'Вы были {text}ы.'
                                                             f'Если произошла ошибка,'
                                                             f' обратитесь к администратору!',
                           reply_markup=ReplyKeyboardRemove())
