from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from app.forms import LoginForm
from app.models import User
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sander'}
    posts = [
        {
            'author': {'username': 'Mark'},
            'body': 'Sander is slim'
        },
        {
            'author': {'username': 'Ronald'},
            'body': 'Mark heeft het al gezegd, maar inderdaad Sander is slim!'
        }
    ]
    return render_template('index.html', title='Grabot', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

