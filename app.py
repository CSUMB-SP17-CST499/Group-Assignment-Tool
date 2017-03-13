import flask, os
from flask import render_template, flash, request, json
from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField, csrf
from wtforms.validators import DataRequired
from slackclient import SlackClient
from hashlib import md5


app = flask.Flask(__name__)


@app.route('/')
def index():
    slack_client = SlackClient('your test token here')
    slack_client.api_call("api.test")
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

    slack_client = SlackClient(SLACK_TOKEN)

# If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("index.html")
    
@app.route('/login')
def login():
# If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("login.html")
    
@app.route('/showcreateaccount')
def showcreateaccount():
    return render_template("createAccount.html")
    
    
@app.route('/createaccount', methods=['POST'])
def createaccount():
    _firstname = request.form['firstname']
    _lastname = request.form['lastname']
    _email = request.form['email']
    username = request.form['username']
    _password = request.form['userPassword']
    if _firstname and _lastname and _email and username and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    return()
    
@app.route('/loginDB', methods=['GET', 'POST'])
def loginBD():
    # #form = LoginForm(request.form)
    # return flask.render_template("login.html", title ="Login", form=form)
    # # print (form.errors)
    # if request.method == 'POST':
    #     if request.form['submit'] == 'Login':
    #         username=request.form['userName']
    #         password=request.form['userPassword']
    #         print (username, " ", password)
    #         return flask.render_template("login.html", title ="Login", form=form)
    #     # if form.validate():
    #     #     flash('Thanks for registration ' + username)
    #     # elif request.form['submit'] == 'Create Account':
    #     #     return render_template('createaccount.html', form=form)
    return flask.render_template("login.html")

@app.route('/add')
def addEmp():
    return flask.render_template("add.html")

@app.route('/employee')
def empGroup():
    return flask.render_template("employee.html")
    
@app.route('/edits')
def edits():
    return flask.render_template("edits.html")


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)