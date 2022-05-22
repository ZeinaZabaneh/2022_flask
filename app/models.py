from app import db
from app import login
from datetime import datetime

from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_IPAddress = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.DateTime, index=True, default=datetime.now)
    score = db.Column(db.Integer)

    def __repr__(self):
        return '<IP_Address {}>'.format(self.user_IPAddress)

class GameUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    plays = db.relationship('Game', backref='played', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Game(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, default=datetime.now)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Score {}>'.format(self.score)

@login.user_loader
def load_user(id):
    return GameUser.query.get(int(id))