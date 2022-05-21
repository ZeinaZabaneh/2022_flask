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