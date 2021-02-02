
def change_availability(message):
    """ Function for admin-changing positions availability """
    from database.connection import cln_item
    position_name = message.text.split(' Наличие')[0]
    try:
        position = cln_item.find_one({'name': position_name}, {'availability': 1})

        if position['availability']:
            cln_item.update_many({'name': f'{position_name}'}, {"$set": {'availability': False}})
            return 'Изменено на "нет" в наличии'

        elif not position['availability']:
            cln_item.update_many({'name': f'{position_name}'}, {"$set": {'availability': True}})
            return 'Изменено на "есть" в наличии'

    # Some positions are tracked by key=name others - key=taste
    except TypeError:
        position = cln_item.find_one({'taste': position_name}, {'availability': 1})

        if position['availability']:
            cln_item.update_many({'taste': f'{position_name}'}, {"$set": {'availability': False}})
            return 'Изменено на "нет" в наличии'

        elif not position['availability']:
            cln_item.update_many({'taste': f'{position_name}'}, {"$set": {'availability': True}})
            return 'Изменено на "есть" в наличии'
