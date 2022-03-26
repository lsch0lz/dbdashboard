import os
from flask import Flask, render_template, request

from controller.database import get_conn
from controller.encryption import verify_password

from model.registration import create_user

app = Flask(__name__)

ahead = ("Abfahrt","Ankunft","Name","Dauer")
adata = (
  ("15:01","18:17","ICE 7731","2:14"),
  ("15:02","18:17","ICE 7732","2:14"),
  ("15:03","18:17","ICE 7733","2:14"),
  ("15:04","18:17","ICE 7734","2:14"),
  ("15:05","18:17","ICE 7735","2:14"),
  ("15:06","18:17","ICE 7736","2:14"),
)

bhead = ("Abfahrt","Bahnhof","Gleis")
bdata = (
  ("07:04 +0","Berlin Hbf (tief)","2"),
  ("07:11 +1","Berlin Südkreuz","3"),
  ("08:18 +2","Halle(Saale)Hbf","6"),
  ("08:50 +5","Erfurt Hbf","1"),
  ("10:56 +5","Frankfurt(Main)Hbf","10")
)

#we define the route /
@app.route('/')
def welcome():
    return render_template('index.html',
                           title="Start")

# login
@app.route('/login')
def check():
    return render_template('login.html',
                           title="Login")

@app.route('/login', methods=['POST'])
def route_verify_password():
    email = request.form['email']
    password = request.form['password']
    val = verify_password(email, password)
    return {'Msg': val}

# signup
@app.route('/signup')
def signup_user():
    return render_template('signup.html',
                           title="Registrieren")

@app.route('/signup', methods=['POST'])
def route_signup_user():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    create_user(name, lastname, email, password)
    return render_template('dashboard.html')

@app.route('/routing')
def routing():
  return render_template('routing.html',
        title="Reiseauskunft", ahead=ahead, adata=adata, bhead=bhead, bdata=bdata)

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html',
        title="Dashboard", ahead=ahead, adata=adata, bhead=bhead, bdata=bdata)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))