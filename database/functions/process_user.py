from database.connection import *


def add_user(message):
    """ Adds info about bot users """
    user_id = message.from_user.id
    db_data = list(cln_user.find({}, {'user_id': 1, 'status': 1}))
    users_id = []
    for user in db_data:
        try:
            users_id.append(user['user_id'])
        except KeyError:
            pass

    from datetime import datetime
    now = datetime.now()
    if user_id not in users_id:
        cln_user.insert({'user_id': user_id, 'first_name': message.from_user.first_name,
                         'last_name': message.from_user.last_name,
                         'username': message.from_user.username,
                         'language_code': message.from_user.language_code,
                         'date_of_adding': now.strftime("%m/%d/%Y, %H:%M:%S"),
                         'chat_link': f'tg://user?id={message.from_user.id}',
                         'status': True
                         })


def whitelist(message):
    user_id = message.from_user.id
    db_data = list(cln_user.find({'user_id': user_id}, {'status': 1}))
    for user in db_data:
        return user['status']


def user_get_status(message):
    user_id = int(message.text)
    db_data = cln_user.find({'user_id': user_id}, {'status': 1})
    for user in db_data:
        return 'Разблокирован' if user['status'] else 'Заблокирован'


def user_change_status(message):
    user_id = int(message)
    db_data = cln_user.find({'user_id': user_id}, {'user_id': 1, 'status': 1})
    for user in db_data:
        cln_user.update({'user_id': user['user_id']}, {'$set': {'status': not user['status']}})
        return 'Разблокирован' if not user['status'] else 'Заблокирован'
