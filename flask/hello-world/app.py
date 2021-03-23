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
def methods_example():
    # Working with POST/GET requests, using the index forms
    if request.method == 'POST':
        if request.form['post-name']:
            return f"Hey, hello {request.form['post-name']} welcome to POST."

        return "POST method was used."

    elif request.method == 'GET':
        if request.args.get('get-name', ''):
            return f"Hey, hello {request.args.get('get-name', '')}, welcome to GET."

        return "GET method was used"

    else:
        return "What heck dude  "
