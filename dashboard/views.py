from flask import Blueprint, request, render_template, abort, url_for
from jinja2 import TemplateNotFound
from db.encode import create_error
from db import query

dashboard = Blueprint('dashboard', __name__,
                        static_url_path='/dashboard/static',
                        template_folder='templates', 
                        static_folder='static',)
                        
@dashboard.route('/<page>')
def show(page):
    try:
        return render_template("%s/view.html" % page)
    except TemplateNotFound:
        return render_template("404.html",)


@dashboard.route('/<page>/add')
def add(page):
    try:
        return render_template("%s/add.html" % page)
    except TemplateNotFound:
        return render_template("404.html")


@dashboard.route('/<page>/update')
def update(page):
    try:
        return render_template("%s/update.html" % page)
    except TemplateNotFound:
        return render_template("404.html")
