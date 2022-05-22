from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import GameUser, Game

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        u1 = GameUser(username='Zeina')
        u2 = GameUser(username='Ben')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        assert u1 in GameUser.query.all()
        assert u2 in GameUser.query.all()

    def test_create_games(self):
        # create four games
        now = datetime.utcnow()
        g1 = Game(date=now, score=5, user_id='john')
        g2 = Game(date=now, score=2, user_id='susan')
        g3 = Game(date=now, score=6, user_id='mary')
        g4 = Game(date=now, score=3, user_id='david')
        db.session.add_all([g1, g2, g3, g4])
        db.session.commit()
        assert g1 in Game.query.all()
        assert g2 in Game.query.all()
        assert g3 in Game.query.all()
        assert g4 in Game.query.all()

if __name__ == '__main__':
    unittest.main(verbosity=2)