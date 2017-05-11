import json
from apis import token
from apis.slack._connection import Connection
from apis.slack._user import User
from apis.slack._usergroup import UserGroup


class SlackClient():
    
    def __init__(self, connection, token):
        self.token = token
        self.connection = connection
        
    
    def get_usergroups_list(self, params = {}):
        method = 'usergroups.list'
        result = json.dumps(self.connection._request(token, method, params))
        
    
    def get_usergroups_users(self, params = {}):
        method = 'usergroups.users.list'
        result = json.dumps(self.connection._request(token, method, params))
        
        
    def get_users_list(self, params = {}):
        method = 'users.list'
        result = json.dumps(self.connection._request(token, method, params))
    
    
    def update_usergroup_users(self, params = {}):
        method = 'usergroups.users.update'
        result = json.dumps(self.connection._request(token, method, params))
    
    
    def _parse_usergroups(self, text):
        pass
    
    
    def _parse_usergroups_users(self, text):
        pass
    
    
    def _parse_users(self, text):
        pass