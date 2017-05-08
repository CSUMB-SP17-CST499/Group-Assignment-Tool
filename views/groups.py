from flask import Blueprint, request
from db.encode import get_json, create_error
from db import query
from db.models import Role
import json


groups = Blueprint('groups', __name__,
                    template_folder='templates')
                    
@groups.route('/api/groups', methods = ['GET'])
def groups_uri():
    if request.method == 'GET':
        try:
            groups = query.get_all_groups()
            return get_json('roles', groups)
            
        except Exception as e:
            print(e)
            response = create_error('unexpected_error', e)
            return (response, 500)
            