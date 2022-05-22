from app import db
from app import login
from datetime import datetime

from flask_login import UserMixin

class GameUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    plays = db.relationship('Game', backref='played', lazy='dynamic')

    def __repr__(self):
        return '<Username {}>'.format(self.username)

class Game(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True)
    score = db.Column(db.Integer)
    user_id = db.Column(db.String(64), db.ForeignKey('game_user.username')) #Note that when using table names with a camel case, Flask-SQLAlchemy converts CamelCase classes to camel_case when creating the table, so when referencing the table in the join, a '_'must be added between the CamelCase words.

    def __repr__(self):
        return '<Score {}>'.format(self.score)

@login.user_loader
def load_user(id):
    return GameUser.query.get(int(id))