import os
from flask import Flask, render_template
app = Flask(__name__)

#we define the route /
@app.route('/')
def welcome():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))