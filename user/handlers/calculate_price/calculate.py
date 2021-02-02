from database.connection import *


def calculate_price(message):
    """Функция возвращает стоимость позиции"""
    price = 0

    # В дессертах на вход идет уже message.text, поэтому на этот случай обрабатываем ошибку
    try:
        position = str(message.text)
    except AttributeError:
        position = str(message)
    db_data = cln_item.find({'name': position.split(" (")[0]}, {'price': 1})
    for i in db_data:
        price = int(i['price'])

    return price
