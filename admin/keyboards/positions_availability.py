from aiogram.types import ReplyKeyboardMarkup

from database.connection import *


def admin_dessert_kb():
    db_data = cln_item.find({"type": "dessert"})
    positions = []

    for position in db_data:
        if position['name'] not in positions:
            positions.append(position['name'])

    dessert_selection_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:
        position = cln_item.find({"name": positions.pop(0)}, {"name": 1, "availability": 1})

        for i in position:
            btn_1 = f'{i["name"]} Наличие: {i["availability"]}'

        dessert_selection_kb.insert(btn_1)

    dessert_selection_kb.row("Назад")

    return dessert_selection_kb


def admin_tea_kb():
    db_data = cln_item.find({"key": "fruit_tea"})
    positions = []

    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    tea_selection_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:
        position = cln_item.find({"taste": positions.pop(0)}, {"taste": 1, "availability": 1})

        for i in position:
            btn_1 = f'{i["taste"]} Наличие: {i["availability"]}'

        tea_selection_kb.insert(btn_1)

    tea_selection_kb.row("Назад")

    return tea_selection_kb


def admin_macaroon_kb():
    db_data = cln_item.find({"key": "macaroon"})
    positions = []

    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    macaroon_selection_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:
        position = cln_item.find({"taste": positions.pop(0)}, {"taste": 1, "availability": 1})

        for i in position:
            btn_1 = f'{i["taste"]} Наличие: {i["availability"]}'

        macaroon_selection_kb.insert(btn_1)

    macaroon_selection_kb.row("Назад")

    return macaroon_selection_kb


def admin_brownie_kb():
    db_data = cln_item.find({"key": "brownie"})
    positions = []

    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    brownie_selection_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    while len(positions) != 0:
        position = cln_item.find({"taste": positions.pop(0)}, {"taste": 1, "availability": 1})

        for i in position:
            btn_1 = f'{i["taste"]} Наличие: {i["availability"]}'

        brownie_selection_kb.insert(btn_1)

    brownie_selection_kb.row("Назад")

    return brownie_selection_kb
