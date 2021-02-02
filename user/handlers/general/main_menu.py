from aiogram.types import Message, ParseMode

from app import bot
from config import working_hours
from database.functions.process_user import add_user, whitelist
from loader import dp
from user.keyboards import kb_main_menu, kb_choose_deliver_type
from user.states import MenuClass, OrderClass


@dp.message_handler(commands=['start'], state='*')
async def start_cmd(message: Message):
    add_user(message)
    if whitelist(message):
        await bot.send_message(chat_id=message.chat.id, text=f"""
    Приветствуем вас, {message.from_user.first_name}, в <b>handbrewcoffee_bot</b>
    
    <i>Вы ходили к нам в гости, теперь мы ходим к вам!</i>  
    
    Нажимайте кнопки и читайте подсказки для того, чтобы сделать заказ!
    ❗ <b>️Заказы принимаются только с 8:00 до 20:00 в будни и с 9:00 до 20:00 в выходные</b> ❗️
    """,
                               reply_markup=kb_main_menu, parse_mode=ParseMode.HTML)
        await MenuClass.Main_menu.set()
    else:
        await bot.send_message(chat_id=message.chat.id, text=f"""
К сожалению, вы были <b>заблокированы</b>. Для решения этой проблемы обратитесь, пожалуйста к любому сотруднику!

С уважением, handbrewcoffee.
""", parse_mode=ParseMode.HTML)


@dp.message_handler(commands=['help'], state='*')
async def help_cmd(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="""
Привествуем вас в <b>handbrewcoffee_bot</b>!
<i>Вы ходили к нам в гости, теперь мы ходим к вам!</i>    

Что я умею?
1. Познакомлю вас с нашем меню.
2. Помогу вам сделать заказ:
    - Принесём кофе домой <b>(Доставка)</b>
    - Сделаем ваш заказ к вашему приходу <b>(Самовынос)</b>
3. Помогу вам найти нас.

Если что-то пошло не так, всегда можно отправить мне <b> /start </b> и мы начнем всё сначала.
""", parse_mode=ParseMode.HTML)


@dp.message_handler(text='Заказать', state=MenuClass.Main_menu)
async def main_menu(message: Message):
    """ Заказать """
    import datetime
    now = datetime.datetime.now()
    if 1 <= now.isoweekday() <= 5:
# Временно доставка ток в выходные

#         if working_hours['weekday']['from'] <= now.hour < working_hours['weekday']['to']:

#             await bot.send_message(chat_id=message.chat.id, text='Выберите способ доставки:\n'
#                                                                  '❗<b>Ваш заказ может попасть в живую очередь и будет '
#                                                                  'выполнен с задержкой! </b>',
#                                    reply_markup=kb_choose_deliver_type, parse_mode=ParseMode.HTML)
#
#             await OrderClass.Order_deliver_type.set()
#
#         else:
#             await bot.send_message(chat_id=message.chat.id, text="""
# К сожалению, в будни мы работаем <b>с 8:00 до 21:00</b>
#
# <i> Будем рады видеть вас в рабочее время! </i>
# """,
#                                    parse_mode=ParseMode.HTML)
        await bot.send_message(chat_id=message.chat.id, text='К сожалению, на данный момент доставка осуществляется '
                                                             'только в выходные!')

    else:
        if working_hours['weekend']['from'] <= now.hour < working_hours['weekend']['to']:
            await bot.send_message(chat_id=message.chat.id, text='Выберите способ доставки',
                                   reply_markup=kb_choose_deliver_type)
            await OrderClass.Order_deliver_type.set()
        else:
            await bot.send_message(chat_id=message.chat.id, text="""
К сожалению, в выходые мы работаем <b>с 9:00 до 21:00</b>

<i> Будем рады видеть вас в рабочее время! </i>
""", parse_mode=ParseMode.HTML)


@dp.message_handler(text=['Наше Меню'], state=MenuClass.Main_menu)
async def main_menu(message: Message):
    """ Наше меню"""
    await bot.send_message(chat_id=message.chat.id, text="""
Вот наше меню:
Напитки:
️Эспрессо (30 мл) 27 грн
Доппио (60 мл) 35 грн
Американо (130 мл) 27 грн
Американо с молоком (150 мл) 30 грн
Макиато (60 мл) 30 грн
Капучино (170 мл) 30 грн
Дабл капучино (330 мл) 45 грн
Латте (330 мл) 35 грн
Флэт уайт (170 мл) 40 грн
Раф-кофе (330 мл) 50 грн
Мокко (330 мл) 55 грн
Фильтр (170 мл) 30 грн
Фильтр (330 мл) 40 грн
Чай (330 мл) 27 грн
Чай фруктовый (330 мл) 37 грн

Десерты:
Брауни – 55 грн
Вафельный торт со сгущенкой – 45 грн
Запеканка – 55 грн
Круассан – 40 грн
Макарун – 40 грн
Орешек со сгущёнкой – 22 грн
Трубочка со сгущенкой – 40 грн
Штоллен – 45 грн
""",
                           reply_markup=kb_main_menu)


@dp.message_handler(text=['Локация'], state=MenuClass.Main_menu)
async def main_menu(message: Message):
    """ Локация """
    await bot.send_venue(chat_id=message.chat.id, latitude=50.417809, longitude=30.63361, title='Hand Brew Coffee',
                         address='вул. Драгоманова, 2А', foursquare_id="5ad7117f0d8a0f343eada3a5",
                         foursquare_type="food/coffeeshop")
