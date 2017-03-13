from flask import Flask
from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField, csrf
from wtforms.validators import DataRequired

app = Flask(__name__)
from app import app


class LoginForm(Form):
    username = TextField(validators=[validators.required()])
    password = TextField(validators=[validators.required(), validators.Length(min=3, max=35)])