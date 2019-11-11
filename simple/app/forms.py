from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import EqualTo
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import ValidationError
from wtforms.validators import Length
from app.models import User


def validate_username(username):
    """
    The user can choose a username when it registers.
    If the username is already taken we give a validation error.
    """
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
        raise ValidationError('Please use a different username.')


def validate_email(email):
    """
    The user can choose an email when it registers.
    If the email is already taken we give a validation error.
    """
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
        raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    """
    The information of the login form.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """
    The information of the Registration form.
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class EditProfileForm(FlaskForm):
    """
    The information of the edit profile page.
    """
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    # The user can change it's username. We need to validate that this name does not exist in the database.
    def validate_username(self, username):
        # If the user leaves its name the same it should not give an error.
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

