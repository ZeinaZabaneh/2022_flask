from flask import render_template, url_for, flash, redirect, jsonify
from flask_login import current_user, login_user
from app.models import Game, GameUser

from app import app 
from app.forms import LoginForm
from datetime import datetime

from flask import request  
def get_ip(): 
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/pass_val',methods=['GET','POST'])
def pass_val():
    value=request.args.get('value')
    print("tried to write")
    gameinfo(value)
    print('value',value)
    return jsonify({'reply':'success'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = GameUser.query.filter_by(username=form.username.data).first()
        if user is None :
            flash('Invalid username')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


from app import db
from app.forms import RegistrationForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = GameUser(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/gameinfo', methods=['GET', 'POST'])
def gameinfo(user_score):
        date = datetime.today()
        print("attempting score")
        score = user_score
        print("defining form")
        #form = RegistrationForm()
        #print("retreiving from form")
        #user_id = form.username.data
        print("current_user.username")
        user_id = current_user.username
        print("usernam retrieved: {}".format(user_id))
        print("creating Game row object")
        game = Game(date = date, score = score, user_id = user_id)
        print("adding row object to database")
        db.session.add(game)
        db.session.commit()

@app.route("/histogram",methods=['GET'])
def histogram():
    data = Game.query.filter_by(user_id=current_user.username)
    scores = [score_entry.score for score_entry in data]
    totals = []
    max_score = 0
    for i in range(1,9):
        score_count = 0
        for score in scores:
            if score==i:
                score_count +=1
        totals.append(score_count)
        if score_count > max_score:
            max_score = score_count

    return(jsonify({"result":totals,"max":max_score}))