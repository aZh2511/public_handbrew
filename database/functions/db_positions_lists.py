from database.connection import cln_item


def drinks_menu():
    """Создает клавиатуру для выбора напитков"""
    db_data = cln_item.find({'type': 'drink'})

    positions = [f'{position["name"]} ({position["measurement_amount"]} {position["measurement_unit"]}) '
                 f'{position["price"]} грн' for position in db_data]
    return set(positions)


def milks_menu():
    """ Создает клавиатуру для выбора молока"""
    db_data = cln_item.find({"type": "milk"})

    positions = []
    for position in db_data:
        if position['price']:
            positions.append(f'{position["name"]} ({position["price"]} грн)')
        else:
            positions.append(f'{position["name"]}')
    return set(positions)


def tea_menu():
    """Создаёт клавиатуру для выбоора обычных чаев"""
    db_data = cln_item.find({"key": "tea"})

    positions = []
    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    return set(positions)


def fruit_tea_menu():
    """Клавиатура выбора фруктовых чаев"""
    db_data = cln_item.find({"key": "fruit_tea", "availability": True})
    positions = []

    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    return set(positions)


def dessert_menu():
    """Клавиатура выбора доступных десертов"""
    db_data = cln_item.find({"type": "dessert", "availability": True})
    positions = []
    for position in db_data:
        if position['name'] not in positions:
            positions.append(f"{position['name']} ({position['price']} грн)")

    return set(positions)


def macaroons_menu():
    """Клавиатура выбора доступных вкусов макарунов"""
    db_data = cln_item.find({"key": "macaroon", "availability": True}, {'taste': 1})
    positions = []
    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    return set(positions)


def brownies_menu():
    """Клавиатура выбора доступных вкусов макарунов"""
    db_data = cln_item.find({"key": "brownie", "availability": True}, {'taste': 1})
    positions = []
    for position in db_data:
        if position not in positions:
            positions.append(position['taste'])

    return set(positions)
