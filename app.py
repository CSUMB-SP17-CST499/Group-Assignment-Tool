import flask, os

from flask import render_template, flash, request, json, make_response, g
from hashlib import md5
from views import employees, groups, roles, users, synced
from dashboard.views import dashboard
from db.database import init_db, Session 
from db import query, models
from db.models import User
from flask_login import LoginManager, login_user , logout_user , current_user


app = flask.Flask(__name__)
app.register_blueprint(roles.roles)
app.register_blueprint(groups.groups)
app.register_blueprint(employees.employees)
app.register_blueprint(users.users)
app.register_blueprint(synced.synced)
app.register_blueprint(dashboard)


app.config['SECRET_KEY'] = "GroupAssignment_Tool_KEY374657*"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/users'

# Initalize the database
init_db()


@app.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def load_user(id):
    return query.get_user_by_id(id)

@app.route('/')
def index():
    # If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("index.html")


@app.teardown_appcontext
def shutdown_session(exception = None):
    Session.remove()


if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )
