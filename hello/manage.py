from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from model.user import User

app = Flask(__name__)
POSTGRES = {
    'user': 'brocastadmin',
    'pw': '9EbgZUyVHGU5d2eX',
    'db': 'brocast',
    'host': 'brocast-1.cg9fwmgrjypi.eu-central-1.rds.amazonaws.com',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()