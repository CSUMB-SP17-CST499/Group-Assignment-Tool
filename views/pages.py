from flask import Blueprint, request
from db.encode import create_error
from db import query

pages = Blueprint('pages', __name__,
                    template_folder='templates')
                    