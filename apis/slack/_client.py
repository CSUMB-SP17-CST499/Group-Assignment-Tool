import json
from apis import token
from apis.slack._connection import SlackConnection
from apis.slack._user import User
from apis.slack._usergroup import UserGroup


class SlackClient():
    
    def __init__(self, slack_token):
        self.slack_token = slack_token
        self.connection = SlackConnection()
        
        
    def request(self, method, params = {}, parse_method = None):
        data = json.loads(self.connection._request(self.slack_token, 
                method, params))
        result = None
        if 'ok' in data and data['ok'] and parse_method:
            result = parse_method(data)
        return result
    
    
    def get_usergroups_list(self):
        method = 'usergroups.list'
        params = {}
        params['include_users'] = True
        usergroups = self.request(method, params, self._parse_usergroups)
        return usergroups
    
    
    def get_usergroups_users(self, usergroup_id = None):
        method = 'usergroups.users.list'
        params = {}
        params['usergroup'] = usergroup_id
        users = self.request(method, params, self._parse_usergroups_users)
        return users
        
        
    def get_users_list(self):
        method = 'users.list'
        params = {}
        users = self.request(method, params, self._parse_users)
        return users
    
    
    def update_usergroup_users(self, usergroup_id, users):
        method = 'usergroups.users.update'
        params = {}
        params['usergroup'] = usergroup_id
        params['users'] = users
        usergroup = self.request(method, params, self._parse_usergroup)
        return usergroup.users
        
        
    def _parse_usergroup(self, data):
        u = None
        if 'usergroup' in data:
            usergroup = data['usergroup']
            slack_id = usergroup['id']
            name = usergroup['name']
            users = usergroup['users']
            u = UserGroup(slack_id = slack_id, name = name, users = users)
        return u
    
    
    def _parse_usergroups(self, data):
        usergroups = []
        if 'usergroups' in data: 
            for usergroup in data['usergroups']:
                slack_id = usergroup['id']
                name = usergroup['name']
                users = usergroup.get('users', [])
                u = UserGroup(slack_id, name, users)
                usergroups.append(u)
        return usergroups
    
    
    def _parse_usergroups_users(self, data):
        users = []
        if 'users' in data:
            users = data['users']
        return users
    
    
    def _parse_users(self, data):
        users = []
        if 'members' in data:
            for member in data['members']:
                slack_id = member['id']
                profile = member['profile']
                first_name = profile.get('first_name', '')
                last_name = profile.get('last_name', '')
                email = profile.get('email', '')
                u = User(slack_id = slack_id, first_name = first_name, 
                        last_name = last_name, email = email)  
                users.append(u)
        return users