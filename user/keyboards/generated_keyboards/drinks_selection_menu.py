from aiogram.types import ReplyKeyboardMarkup

from database.connection import *


def create_drinks_kb():
    """Создает клавиатуру для выбора напитков"""
    db_data = cln_item.find({'type': 'drink'})

    positions = []
    for position in db_data:
        if position['name'] not in positions:
            positions.append(position['name'])

    drink_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:
        position = cln_item.find({'name': positions.pop(0)}, {"name": 1, "price": 1, "measurement_unit": 1,
                                                              "measurement_amount": 1})
        for i in position:
            btn_1 = f"{i['name']} ({i['measurement_amount']} {i['measurement_unit']}) {i['price']} грн"

        drink_kb.insert(btn_1)

    return drink_kb


def create_milk_kb():
    """ Создает клавиатуру для выбора молока"""
    db_data = cln_item.find({"type": "milk"})
    positions = []

    for position in db_data:
        if position not in positions:
            positions.append(position['name'])

    milk_selection_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:
        position = cln_item.find({"name": positions.pop(0)}, {"name": 1, "price": 1})

        for i in position:
            if i['price'] != 0:
                btn_1 = f'{i["name"]} ({i["price"]} грн)'
            else:
                btn_1 = f'{i["name"]}'

        milk_selection_kb.insert(btn_1)

    return milk_selection_kb


def create_tea_kb():
    """Создаёт клавиатуру для выбоора обычных чаев"""
    db_data = cln_item.find({"key": "tea"})

    positions = []
    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    tea_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    """Можно очнь упростить, ибо сразу достаю из БД taste (вкусы)"""
    while len(positions) != 0:
        position = cln_item.find({'taste': positions.pop(0)}, {"taste": 1})
        for i in position:
            btn_1 = f"{i['taste']}"

        tea_kb.insert(btn_1)

    return tea_kb


def create_fruit_tea_kb():
    """Клавиатура выбора фруктовых чаев"""
    db_data = cln_item.find({"key": "fruit_tea", "availability": True})
    positions = []

    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    tea_selection_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:
        position = cln_item.find({"taste": positions.pop(0)}, {"taste": 1, "availability": 1})

        for i in position:
            btn_1 = f'{i["taste"]}'

        tea_selection_kb.insert(btn_1)

    return tea_selection_kb
