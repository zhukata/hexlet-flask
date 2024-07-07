import uuid
import json


def filter_users(users, term):
    filtred_users = []

    if not users:
        return filtred_users

    if not term:
        term = ""

    print(users)
    for id, user in users.items():
        print(type(user))
        print(user)
        if user:
            decode_user = json.loads(user)
    
        if decode_user.get('name').lower().startswith(term.lower()):
            filtred_users.append(
                {"id": id, "name": decode_user["name"], "email": decode_user["email"]}
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
    return json.dumps({'name': user['name'], 'email': user['email']})
