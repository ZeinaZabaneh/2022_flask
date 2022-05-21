from flask import render_template, url_for, flash, redirect

from app import app 

from flask import request  
def get_ip(): 
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')


import jsonify

@app.route('/pass_val',methods=['POST'])
def pass_val():
    name=request.args.get('value')
    print('value',name)
    #return jsonify({'reply':'success'})
