import os
from flask import Flask, render_template, request

from controller.database import get_conn
from controller.encryption import verify_password

from model.registration import create_user

app = Flask(__name__)

#we define the route /
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def route_create_user():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    create_user(name, lastname, email, password)
    return render_template('index.html')

# login
@app.route('/login')
def check():
    return render_template('pwd.html')

@app.route('/check', methods=['POST'])
def route_verify_password():
    email = request.form['email']
    password = request.form['password']
    val = verify_password(email, password)
    return {'Msg': val}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))