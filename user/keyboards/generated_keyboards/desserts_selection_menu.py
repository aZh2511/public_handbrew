from aiogram.types import ReplyKeyboardMarkup

from database.connection import *


def create_dessert_kb():
    """Клавиатура выбора доступных десертов"""
    db_data = cln_item.find({"type": "dessert", "availability": True})
    positions = []
    for position in db_data:
        if position['name'] not in positions:
            positions.append(position['name'])

    dessert_availability_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:

        position = cln_item.find({"name": positions.pop(0)}, {"name": 1, "price": 1})

        for i in position:
            btn_1 = f'{i["name"]} ({i["price"]} грн)'

        dessert_availability_kb.insert(btn_1)

    dessert_availability_kb.row('Не нужно')

    return dessert_availability_kb


def create_macaroon_kb():
    """Клавиатура выбора доступных вкусов макарунов"""
    db_data = cln_item.find({"key": "macaroon", "availability": True}, {'taste': 1})
    positions = []
    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    macaroon_availability_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:

        position = cln_item.find({"taste": positions.pop(0)}, {"taste": 1})

        for i in position:
            btn_1 = f'{i["taste"]}'

        macaroon_availability_kb.insert(btn_1)

    return macaroon_availability_kb


def create_brownie_kb():
    """Клавиатура выбора доступных вкусов макарунов"""
    db_data = cln_item.find({"key": "brownie", "availability": True}, {'taste': 1})
    positions = []
    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    brownie_availability_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:

        position = cln_item.find({"taste": positions.pop(0)}, {"taste": 1})

        for i in position:
            btn_1 = f'{i["taste"]}'

        brownie_availability_kb.insert(btn_1)

    return brownie_availability_kb
