from flask import render_template, flash, redirect, request
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mark'}

    posts = [
        {
            'author': {'username': 'Frank'},
            'body': 'Sander kan goed coden!'
        },
        {
            'author': {'username': 'Ronald'},
            'body': 'Sander maakt heel vaak ontzettend goeie grappen'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

