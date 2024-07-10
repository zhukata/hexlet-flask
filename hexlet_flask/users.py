import uuid
import json


users_list = [
    {'name': 'mike', 'email': 'mike@12345.com'},
    {'name': 'mishel', 'email': 'mishel@12345.com'},
    {'name': 'adel', 'email': 'adel@12345.com'},
    {'name': 'keks', 'email': 'keks@12345.com'},
    {'name': 'kamila', 'email': 'kamila@12345.com'},
]


def filter_users(users, term):
    filtred_users = []

    if not users:
        return filtred_users

    if not term:
        term = ""

    print(users)
    decode_user = json.loads(users)
    print(decode_user)
    for id, user in decode_user.items():
        print(type(user))
        print(user)
        if user.get("name").lower().startswith(term.lower()):
            filtred_users.append(
                {
                    "id": id,
                    "name": user["name"],
                    "email": user["email"],
                }
            )
    return filtred_users


def validate(user):
    errors = {}
    if not user.get('name'):
        errors['name'] = "Can't be blank"
    if not user.get('email'):
        errors['email'] = "Can't be blank"
    return errors


def get_id():
    return str(uuid.uuid4())


def encoded_user(user):
    return json.dumps({get_id(): {'name': user['name'], 'email': user['email']}})


def get_user(form_data, repo):
    name = form_data['name']
    email = form_data['email']
    for user in repo:
        if user['name'] == name and user['email'] == email:
            return user
