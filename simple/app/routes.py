from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import request
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import EditProfileForm
from app.models import User
from app import app
from app import db
from datetime import datetime


@app.route('/')
@app.route('/index')
@login_required
def index():
    """
    The homepage of a user. Here, for instance, the posts he made are shown
    """
    # TODO @Sander: Create a way for users to post their own stuff and remove this 'posts' placeholder
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
    return render_template('index.html', title='Grabot', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    The login page. here the get and posts calls are handled using the flask_login package
    So going to the login page and the validation and loggin in.
    If the log in information is not valid it shows an error and you can try again
    If the log in information is correct the user goes to the main page of the user.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    """
    If the user selects 'logout' the logging out is done. This is handled here using the flask_login package
    """
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Here the registration is handled.
    The username, email and possword are validated and check if they don't already exist
    If the registration is succesfull the succes message is shown and the data is included in the database.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    """
    Here the profile page of the logged in user is handled.
    Here the posts made by the user are shown along with the avatar.
    The user can edit his information with the edit information link.
    """
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.before_request
def before_request():
    """
    This is executed right before the view function. Here we set the last_seen variable for the user.
    """
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """
    Here the edit profile page is handled.
    The user can change it's username and it's about page.
    """
    # We pass the current user to the form for the validation.
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))

