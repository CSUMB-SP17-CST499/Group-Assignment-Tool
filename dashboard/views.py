from flask import Blueprint, request, render_template, abort, url_for, g, redirect
from jinja2 import TemplateNotFound
from db.encode import create_error
from flask_login import  login_required, current_user, logout_user
from db import query

dashboard = Blueprint('dashboard', __name__,
                        static_url_path='/dashboard/static',
                        template_folder='templates', 
                        static_folder='static',)


@dashboard.before_request
def before_request():
    g.user = current_user
    
@dashboard.route('/<page>')
def show(page):
    user = g.user
    try:
        return render_template("%s/view.html" % page,
                           user=user)
    except TemplateNotFound:
        return render_template("404.html",)


@dashboard.route('/<page>/add')
@login_required

def add(page):
    user = g.user
    try:
        return render_template("%s/add.html" % page,
                           user=user)
    except TemplateNotFound:
        return render_template("404.html")

@dashboard.route('/<page>/update')
@login_required
def update(page):
    try:
        return render_template("%s/update.html" % page)
    except TemplateNotFound:
        return render_template("404.html")
        
@dashboard.route('/logout')
def logout():
    logout_user()
    return redirect('/')
