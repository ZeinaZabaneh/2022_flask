from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_IPAdress = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.DateTime, index=True, default=datetime.now)
    score = db.Column(db.Integer)

    def __repr__(self):
        return '<Score {}>'.format(self.score)