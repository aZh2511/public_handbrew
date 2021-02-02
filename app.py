# - *- coding: utf- 8 - *-
import datetime

from aiogram import executor

from config import admin_id
from loader import bot, storage

time_of_work = datetime.datetime.now()


async def send_to_admin(dp):
    import datetime
    now = datetime.datetime.now()
    await bot.send_message(chat_id=admin_id, text=f'Бот запущен\n{now}')


async def finish(dp):
    import datetime
    now = datetime.datetime.now()
    await bot.send_message(chat_id=admin_id, text=f'Бот выключен\n{now}'
                                                  f'\n\nВремя работы: {now - time_of_work}')
    await storage.close()
    #await bot.send_message(chat_id=-1001086732377,
                           #text='Меня выключают(\nМеня всё еще не разместили на сервере')


if __name__ == '__main__':
    from user import dp
    from admin import dp
    executor.start_polling(dp, on_startup=send_to_admin, skip_updates=True,
                           on_shutdown=finish)

