from flask import Blueprint, request
from db import query
from db.models import Employee, Group
from synchronization import sync
import json

synced = Blueprint('synced', __name__,
                    template_folder='templates')
                    
                    
@synced.route('/api/sync/groups', methods = ['GET'])
def sync_groups():
    try:
        sync.sync_slack_groups()
    except:
        response = json.dumps({'ok': False})
        return (response, 500)
    
    response = json.dumps({'ok': True})
    return (response, 200)
    
    
@synced.route('/api/sync/users', methods = ['GET'])
def sync_users():
    try:
        sync.sync_slack_users()
    except:
        response = json.dumps({'ok': False})
        return (response, 500)
    
    response = json.dumps({'ok': True})
    return (response, 200)