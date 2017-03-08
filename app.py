import flask, os, flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app) 

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

    
@socketio.on('connect')
def on_connect():
    print('Server says that a client connected.')

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )