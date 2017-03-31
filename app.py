import flask, os

from flask import render_template, flash, request, json, make_response
from hashlib import md5

from db.database import init_db, db_session
from db import query

app = flask.Flask(__name__)

# Initalize the database
init_db()

@app.route('/')
def index():
    # If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("index.html")
    
    
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
                resp = json.dumps({'message': 'The entered email is already in use.' +
                        ' Please entere a different one.'})
                return (resp, 400)
            
            resp = json.dumps({'message': 'Unkown error. Please contact support.'})
            return (resp, 500)
            
        else:
            resp = json.dumps({'message': 'There is a missing field. ' +
                    'Please fill all required fields'})
            return (resp, 400)
            
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':        
        username = request.form['username']
        password = request.form['password']
        
        if False:
            error = 'Unkown error. Please contact support.'
        else:
            flask.redirect('/')

    return flask.render_template('login.html', message = error)


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
