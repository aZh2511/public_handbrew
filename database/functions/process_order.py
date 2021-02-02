from database.connection import *


def add_order(message, data):
    from datetime import datetime
    now = datetime.now()
    cln_order.insert({
        'user_id': message.from_user.id,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
        'language_code': message.from_user.language_code,
        'date_of_order': now.strftime("%m/%d/%Y, %H:%M:%S"),
        'chat_link': f'tg://user?id={message.from_user.id}',
        'order_type': data.get('order_type'),
        'drinks': str(data.get('full_drink')).replace('\n', ' '),
        'drinks_price': data.get('price'),
        'desserts': str(data.get('dessert_order')).replace('\n', ' '),
        'desserts_price': data.get('dessert_price'),
        'house': data.get('chosen_house'),
        'entrance': data.get('chosen_entrance'),
        'floor': data.get('floor'),
        'apartment': data.get('apartment_number'),
        'when_to_deliver': data.get('chosen_time'),
        'comments': data.get('additional_comments'),
        'order_price': int(data.get('total_price')-20 if data.get('order_type') == 'delivery'
                           else data.get('total_price')),
        'delivery_price': int(20 if data.get('order_type') == 'delivery' else 0),
        'price': (data.get('price') + data.get('dessert_price'))
    })
