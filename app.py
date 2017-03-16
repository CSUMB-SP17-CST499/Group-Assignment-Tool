import flask, os

app = flask.Flask(__name__)

@app.route('/base')
def menuBar():
    return flask.render_template("base.html")
    
@app.route('/')
def index():
    return flask.render_template("index.html")
    
@app.route('/login')
def login():
# If there is no userName, then route to loginScreen. Else, route to the main page.
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