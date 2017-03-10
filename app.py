import flask, os
from flask import render_template, flash, request
from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField
from slackclient import SlackClient

app = flask.Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    # email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

@app.route('/')
def index():
    slack_client = SlackClient('your test token here')
    slack_client.api_call("api.test")
    SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

    slack_client = SlackClient(SLACK_TOKEN)
# If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("index.html")
    
@app.route('/login', methods=['GET', 'POST'])
def login():
# If there is no userName, then route to loginScreen. Else, route to the main page.
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        if request.form['submit'] == 'Login':
            name=request.form['userName']
            password=request.form['userPassword']
            print (name, " ", password)
 
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        elif request.form['submit'] == 'Create Account':
            return render_template('createaccount.html', form=form)
    return flask.render_template("login.html")

@app.route('/add')
def addEmp():
    return flask.render_template("add.html")

@app.route('/employee')
def empGroup():
    return flask.render_template("employee.html")

@app.route('/base')
def menuBar():
    return flask.render_template("base.html")
    
@app.route('/edits')
def edits():
    return flask.render_template("edits.html")




app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)