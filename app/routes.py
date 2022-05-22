from flask import render_template, url_for, flash, redirect, jsonify
from flask_login import current_user, login_user
from app.models import GameUser

from app import app 
from app.forms import LoginForm

from flask import request  
def get_ip(): 
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/pass_val',methods=['POST'])
def pass_val():
    name=request.args.get('value')
    print('value',name)
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