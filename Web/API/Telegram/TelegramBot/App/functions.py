import json


def print_struct(struct):
    print(json.dumps(struct, indent=4))


def find_user_by_chat_id(users, chat_id):
    """
    return:
        User if founded
        None if not
    """
    for user in users:
        if user.chat_id == chat_id:
            return user
    return None


def create_keyboard(table):
    """
    table:
    [
     ['Грати', 'Магазин'],
     ['Вихід']
    ]
    return: JSON
    '{
      "keyboard": [
        [{"text": "Грати"}, {"text":  "Магазин"}],
        [{"text": "Вихід"}]
      ]
    }'
    """
    keyboard = []
    for row_with_strings in table:
        row_with_dicts = []
        for string in row_with_strings:
            dct = {'text': string}
            row_with_dicts.append(dct)
        keyboard.append(row_with_dicts)

    return json.dumps({'keyboard': keyboard})


def find_lobby_by_id(lobbies, id_):
    for lobby in lobbies:
        if lobby.id == id_:
            return lobby
    return None
