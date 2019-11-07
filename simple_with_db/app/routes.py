from flask import render_template
from app import app

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

