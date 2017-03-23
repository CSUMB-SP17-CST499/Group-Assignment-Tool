import flask, os

from flask import render_template, flash, request, json, make_response
from flaskext.mysql import MySQL
from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField, csrf
from wtforms.validators import DataRequired
from hashlib import md5

from db.database import init_db, db_session
from db import query



mysql = MySQL()
app = flask.Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'thedirtyham'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PAnthony38'
app.config['MYSQL_DATABASE_DB'] = 'groupAssignmentTool'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# Initalize the database
init_db()

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
    
    if request.method == 'POST':
        data = request.get_json()

        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        is_admin = data.get('is_admin')
        
        if firstname and lastname and email and username and password:
            if query.does_user_email_exist(email):
                data = json.dumps({'message': 'The entered email is already in use.' +
                        ' Please entere a different one.'})
                return (data, 400)
            
            return (json.dumps({'message': 'Unidentified error'}), 500)
            
        else:
            data = json.dumps({'message': 'There is a missing field. ' +
                    'Please fill all required fields'})
            return (data, 400)
            
    
@app.route('/login', methods=['POST'])
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


@app.teardown_appcontext
def shutdown_session(exception = None):
    db_session.remove()


if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )