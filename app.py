import flask, os

from flask import render_template, flash, request, json, make_response
from hashlib import md5

from views.roles import roles
from views.employees import employees
from views.users import users
from dashboard.views import dashboard
from db.database import init_db, Session 
from db import query, models
from db.models import User



app = flask.Flask(__name__)
app.register_blueprint(roles)
app.register_blueprint(employees)
app.register_blueprint(dashboard)
app.register_blueprint(users)

# Initalize the database
init_db()

@app.route('/')
def index():
    # If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("index.html")
    
@app.route('/edits')
def edits():
    return flask.render_template("edits.html")


@app.teardown_appcontext
def shutdown_session(exception = None):
    Session.remove()


if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )
