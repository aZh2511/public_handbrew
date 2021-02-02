from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_choose_deliver_type = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Самовынос'), KeyboardButton(text='Доставка')]
], resize_keyboard=True)

kb_order_more = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да'), KeyboardButton(text='Нет')],
    [KeyboardButton(text='Заново'), KeyboardButton(text='Отмена')]
], resize_keyboard=True)

kb_choose_house = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Драгоманова 2'), KeyboardButton(text='Драгоманова 2А')],
    [KeyboardButton(text='Драгоманова 2Б'), KeyboardButton(text='Драгоманова 4А')],
    [KeyboardButton(text='Пчелки 8')]
], resize_keyboard=True)

kb_choose_entrance = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Первый'), KeyboardButton(text='Второй'), KeyboardButton(text='Третий')]
], resize_keyboard=True)

kb_additional_comments = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Нет')]
], resize_keyboard=True)

kb_choose_time = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Через 10 минут'), KeyboardButton(text='Через 15 мин')],
    [KeyboardButton(text='Через 20 минут'), KeyboardButton(text='Через 25 мин')]
], resize_keyboard=True)

kb_self_delivery_time = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Сейчас'), KeyboardButton(text='Через 5 минут')],
    [KeyboardButton(text='Через 10 минут')]
], resize_keyboard=True)

kb_choose_qnt_dessert = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='1'), KeyboardButton(text='2')]
], resize_keyboard=True)

kb_specify_order = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Всё верно'), KeyboardButton(text='Заново')],
    [KeyboardButton(text='Отмена')]
], resize_keyboard=True)

kb_main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Наше Меню'), KeyboardButton(text='Заказать')],
    [KeyboardButton(text='Локация'), KeyboardButton(text='')]
], resize_keyboard=True)


kb_admin_panel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Наличие')]
], resize_keyboard=True)
