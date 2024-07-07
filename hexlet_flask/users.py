def filter_users(users, term):
    filtred_users = []
    if not term:
        return users
    for user in users:
        # if term.lower() in i['first_name'].lower():
        #     filtred_users.append(i['first_name'])
        if user.lower().startswith(term.lower()):
            filtred_users.append(user)
    return filtred_users


def validate(user):
    errors = {}
    if not user.get('name'):
        errors['name'] = "Can't be blank"
    if not user.get('email'):
        errors['email'] = "Can't be blank"
    return errors
