from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

application = app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app)

POSTGRES = {
    'user': 'brocastadmin',
    'pw': '9EbgZUyVHGU5d2eX',
    'db': 'brocast',
    'host': 'brocast-1.cg9fwmgrjypi.eu-central-1.rds.amazonaws.com',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


class HelloWorld(Resource):
    def get(self):
        return {"about": "Hello World!"}


api.add_resource(HelloWorld, "/")


class Users(Resource):
    def get(self):
        users = User.query.all()
        return {"users": users}


api.add_resource(Users, "/bros")


from model.user import User

if __name__ == "__main__":
    app.run()

