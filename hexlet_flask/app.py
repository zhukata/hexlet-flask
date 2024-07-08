from flask import (
    Flask,
    flash,
    make_response,
    render_template,
    request,
    session,
    url_for,
    redirect,
)

from hexlet_flask import users

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key'


@app.route('/')
def index():
    current_user = session.get('user')
    return render_template(
        'index.html',
        current_user=current_user,
        )


@app.get('/users')
def users_get():
    term = request.args.get('term')
    users_list  = request.cookies.to_dict()
    filtred_users = users.filter_users(users_list, term)

    return render_template(
        'users/users.html',
        search=term,
        filtred_users=filtred_users
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
    
    response = make_response(redirect(url_for('users_get'), code=302))
    response.set_cookie(users.get_id(), users.encoded_user(user))
    flash('Пользователь успешно добавлен', 'success')
    return response

@app.get('/users/int:<id>')
def user_id(id):

    return render_template(
        'users/show.html',
        id=id,
    )


@app.get('/users/new')
def new_user():
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
    

@app.post('/users/clean/int:<id>')
def users_clean(id):
    response = redirect(url_for('users_get'))
    response.delete_cookie(str(id))
    return response


@app.post('/session/new')
def new_session():
    data = request.form.to_dict()
    user = users.get_user(data, users.users_list)
    if user:
        session['user'] = user
    else:
        flash('Wrong email or name.')

    return redirect(url_for('index'))


@app.route('/session/delete', methods = ['POST', 'DELETE'])
def delete_session():
    session.pop('user')
    return redirect(url_for('index'))