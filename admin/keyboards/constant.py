from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_admin_panel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Наличие'), KeyboardButton(text='Вайтлист')]
], resize_keyboard=True)

kb_availability_choose = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Десерты'), KeyboardButton(text='Чаи')],
    [KeyboardButton(text='Макаруны'), KeyboardButton(text='Брауни')]
], resize_keyboard=True)

kb_whitelist = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Заблокировать / Разблокировать')]
], resize_keyboard=True)
