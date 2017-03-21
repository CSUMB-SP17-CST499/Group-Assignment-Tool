import flask, os

from flask import render_template, flash, request, json
from flaskext.mysql import MySQL
from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField, csrf
from wtforms.validators import DataRequired
from hashlib import md5


mysql = MySQL()
app = flask.Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'thedirtyham'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PAnthony38'
app.config['MYSQL_DATABASE_DB'] = 'groupAssignmentTool'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index():
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
    # return json.dumps({'status':'OK','user':_firstname,'pass':_lastname});
    _email = request.form['email']
    username = request.form['username']
    _password = request.form['userPassword']
    if _firstname and _lastname and _email and username and _password:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from User where Username = ' " + username + " ' ");
        data = cursor.fetchone()
        if data is None:
            cursor.callproc('sp_createUser',(_firstname, _lastname, _email, username, _password));
        else:
            return "Username already exists"
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    return render_template("login.html")
    
    
@app.route('/loginDB', methods=['POST'])
def loginBD():
    username = request.form['userName']
    password = request.form['userPassword']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where user_username = ' " + username + " ' and user_password = ' " + password + " ' ")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return flask.render_template("index.html")
    return json.dumps({'status':'OK','user':username,'pass':password});


@app.route('/add')
def addEmp():
    return flask.render_template("add.html")


@app.route('/employee')
def empGroup():
    return flask.render_template("employee.html")
    
    
@app.route('/edits')
def edits():
    return flask.render_template("edits.html")


if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )