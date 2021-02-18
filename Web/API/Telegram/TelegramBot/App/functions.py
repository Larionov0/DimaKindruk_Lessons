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
