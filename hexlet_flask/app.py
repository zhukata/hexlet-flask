from flask import Flask, render_template, request, url_for, redirect

# Это callable WSGI-приложение
app = Flask(__name__)

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

@app.route('/')
def index():
    return 'Welcome to Flask!'


@app.get('/users')
def users_get():
    term = request.args.get('term')

    return render_template(
        'users/index.html',
        users=users,
        search=term,
        filtred_users=filter_users(users, term)
    )


@app.route('/users/<id>')
def user_id(id):

    return render_template(
        'users/show.html',
        id=id,
    )


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'


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
