from application import db


class User(db.Model):
    """
    Bro that is stored in the database.
    The bro has a unique id and bro name
    The password is hashed and it can be checked.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)

