from flask import Flask
from flask import request, LoginForm, valid_login, log_the_user_in
from flask import render_template, LoginManager

app = Flask(__name__)



@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    
    if request.method == 'POST':
        if valid_login(request.form['userName'],
                       request.form['passWord']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
    
    
@app.route('/')
def my_form():
    return render_template("LoginScreen.html")

@app.route('/', methods=['POST'])
def my_form_post():

    userName = request.form['userName']
    password = request.form['userPassword']
    return userName

if __name__ == '__main__':
    app.run()
