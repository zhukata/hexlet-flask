from flask import Flask, flash, render_template, request, url_for, redirect

from hexlet_flask import users

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key'

users_list = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/')
def index():
    return render_template('form.html')


@app.get('/users')
def users_get():
    term = request.args.get('term')

    return render_template(
        'users/index.html',
        users=users,
        search=term,
        filtred_users=users.filter_users(users_list, term)
    )


@app.post('/users')
def post_users():
    user = request.form.to_dict()
    errors = users.validate(user)
    if errors:
        return render_template(
          'users/new.html',
          user=user,
          errors=errors,
        ), 422
    
    # repo.save(user)
    flash('Пользователь успешно добавлен', 'success')
    return redirect(url_for('users_get'), code=302)

@app.get('/users/int:<id>')
def user_id(id):

    return render_template(
        'users/show.html',
        id=id,
    )


@app.get('/users/new')
def get_user():
    user = {
        'name': '',
        'email' : ''
    }
    errors = {}

    return render_template(
        'users/new.html',
        user=user,
        errors=errors
    )
