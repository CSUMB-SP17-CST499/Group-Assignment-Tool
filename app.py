import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
# If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("LoginScreen.html")

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)