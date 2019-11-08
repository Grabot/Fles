from flask import render_template, flash, redirect
from app.forms import LoginForm
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

