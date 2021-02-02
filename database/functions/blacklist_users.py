from database.connection import cln_user


def black_list():
    data = cln_user.find({'status': False}, {'user_id': 1, 'first_name': 1, 'username': 1})
    banned_users = [f'Айди: {user["user_id"]} Имя: {user["first_name"]} @{user["username"]}' for user in data]
    text = ''
    for user in banned_users:
        text += f'{user}\n'
    if text:
        return text
    return ''
