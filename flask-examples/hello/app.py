from flask import Flask, url_for, render_template

app = Flask(__name__)

# Standard Flask routing system
@app.route('/hello/')
def hello_world():
    return 'Hello World with Flask'

# Using HTML templates
@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

# Using HTTP methods
from flask import request

@app.route('/method/', methods=['GET', 'POST'])
def goodbye():
    if request.method == 'POST':
        return 'POST method was used'
    elif request.method == 'GET':
        return 'GET method was used'
    else:
        return 'I really dont know'
