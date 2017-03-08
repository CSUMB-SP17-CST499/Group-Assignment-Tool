import flask, os

app = flask.Flask(__name__)

@app.route('/')
def index():
# If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("LoginScreen.html")

@app.route('/AddPermissions')
def addPermissions():
    return flask.render_template("AddPermissions.html")

@app.route('/Employeepermissions')
def empPermissions():
    return flask.render_template("Employeepermissions.html")

@app.route('/Menubar')
def menuBar():
    return flask.render_template("Menubar.html")


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)