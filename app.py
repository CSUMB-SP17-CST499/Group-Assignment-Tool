import flask, os
from flask import render_template, flash, request
from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField, csrf
from slackclient import SlackClient

from hashlib import md5


app = flask.Flask(__name__)


SECRET_KEY = '1234567890'

# class IPAddressCSRF(csrf):
#     """
#     Generate a CSRF token based on the user's IP. I am probably not very
#     secure, so don't use me.
#     """
#     def setup_form(self, form):
#         self.csrf_context = form.meta.csrf_context
#         return super(IPAddressCSRF, self).setup_form(form)

#     def generate_csrf_token(self, csrf_token):
#         token = md5(SECRET_KEY + self.csrf_context).hexdigest()
#         return token

#     def validate_csrf_token(self, form, field):
#         if field.data != field.current_token:
#             raise ValueError('Invalid CSRF')

class LoginForm(Form):
    username = TextField(validators=[validators.required()])
    password = TextField(validators=[validators.required(), validators.Length(min=3, max=35)])

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
    
@app.route('/loginDB', methods=['GET', 'POST'])
def loginBD():
    form = LoginForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        if request.form['submit'] == 'Login':
            username=request.form['userName']
            password=request.form['userPassword']
            print (username, " ", password)
            return flask.render_template("login.html", form=form)
        if form.validate():
            flash('Thanks for registration ' + username)
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