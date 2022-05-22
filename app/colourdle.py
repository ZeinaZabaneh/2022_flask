from app import app, db
from app.models import Game, GameUser

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'GameUser' : GameUser, 'Game' : Game}