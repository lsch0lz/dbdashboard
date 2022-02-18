import os
from flask import Flask, render_template, request
from controller.database import get_conn
from model.registration import create_user

app = Flask(__name__)

#we define the route /
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    create_user(name, lastname, email, password)
    return {'Message': 'OK'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))