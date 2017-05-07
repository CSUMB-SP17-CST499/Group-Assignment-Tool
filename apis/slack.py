import requests
from apis import token

  
def get_user_groups():
    """Function creates a 'get'reques by passing the token as a parameter for authentication.

    Args:
        none

    Returns:
        Returns a list containing Slack group names.

    """
    request = requests.get('https://slack.com/api/usergroups.list', 
            params = {'token': token.get_slack_token() },
            headers = {'Connection': 'close'} )
            
    data = request.json()
    names = []
    size = len(data)
    for i in range (0, size):
       names.append(data['usergroups'][i]['name'])
    return names
    
def get_user_group_ids():
    """Function creates a 'get'request by passing the token as a parameter for authentication.

    Args:
        none

    Returns:
        Returns a list containing Slack group ids.

    """
    request = requests.get('https://slack.com/api/usergroups.list', 
            params = {'token': token.get_slack_token() },
            headers = {'Connection': 'close'} )
            
    data = request.json()
    group_ids = []
    size = len(data)
    for i in range (0, size):
       group_ids.append(data['usergroups'][i]['id'])
    return group_ids
    
def get_users(group):
    """Function creates a 'get'reques, in order to obtain the group user's names, by passing the token as a parameter for authentication and the
        ids of the group members.

    Args:
        param1 (list): the name of the group

    Returns:
        Returns a list containing the names of the members in the Slack group specified.

    """
    users_names = []
    try:
        request = requests.get('https://slack.com/api/usergroups.list', 
                params = {'token': token.get_slack_token(), 'include_users': "true"},
                headers = {'Connection': 'close'} )
                
        data = request.json()
        names = []
        size = len(data)

        group_id = ""
        for i in range (0, size):
            if group == data['usergroups'][i]['name']:#if the passed in group is equal to a group found in the api request
                users_names = get_user_names(data['usergroups'][i]['users'])
                break
    except requests.exceptions.RequestException as e:
        print(e)
    
    return users_names
    
def get_user_ids(group):
    """Function creates a 'get'reques, in order to obtain the group user's names, by passing the token as a parameter for authentication and the
        ids of the group members.

    Args:
        param1 (list): the name of the group

    Returns:
        Returns a list containing the names of the members in the Slack group specified.

    """
    user_ids = []
    try:
        request = requests.get('https://slack.com/api/usergroups.users.list', 
                params = {'token': token.get_slack_token(), 'usergroup': group},
                headers = {'Connection': 'close'} )
                
        data = request.json()
        user_ids = data['users']

    except requests.exceptions.RequestException as e:
        print(e)
        
    return user_ids

def get_user_names(user_ids):
    """Function creates a 'get'reques, in order to obtain the group user's names, by passing the token as a parameter for authentication.

    Args:
        param1 (:list:`str`)

    Returns:
        Returns a list containing the names of the members in the Slack group specified.

    """
    users_names = []
    for id in user_ids: #doing an api reques per user
        try:
            request = requests.get('https://slack.com/api/users.info', 
                    params = {'token': token.get_slack_token(), 'user': id},
                    headers = {'Connection': 'close'} )
                    
            data = request.json()
            users_names.append(data['user']['name'])
            
        except requests.exceptions.RequestException as e:
            print(e)
            
    return users_names
    
def update_usergroup_users(user_group_id, user_ids):
    """Function creates a 'get' request, in order to update the list of user in a user group, by passing the token as a parameter for authentication,
        a list of userIDs, and the id of the user_group.

    Args:
        user_ids: A list of user ids to be used to update the 
            users belonging to a group.
        user_group_id: The id of the user group the users will
            be added to.

    Returns:
        Returns a list containing the names of the members in the 
        Slack group specified.
    """
    data = []
    try:
        request = requests.get('https://slack.com/api/usergroups.users.update', 
                params = {'token': token.get_slack_token(), 
                        'usergroup': user_group_id, 
                        'users': user_ids},
                headers = {'Connection': 'close'} )
                
        data = request.json()
        
    except requests.exceptions.RequestException as e:
        print(e)
            
    return data
    

def get_user_list():
    """Function creates a 'get'request, in order to get all the information from the users in the Slack channel,
    by passing the token as a parameter for authentication.

    Args:
        none

    Returns:
        Returns a dictionary containing the information of all users in the slack channel.

    """
    data = []
    try:
        request = requests.get('https://slack.com/api/users.list', 
                params = {'token': token.get_slack_token()},
                headers = {'Connection': 'close'} )
                
        data = request.json()
    
    except requests.exceptions.RequestException as e:
        print(e)
    
    return data
    
    
def get_user_groups_list():
    """Function creates a 'get'request, in order to get all the information from the groups in the Slack channel,
    by passing the token as a parameter for authentication.

    Args:
        none

    Returns:
        Returns a dictionary containing the information of all groups in the slack channel.

    """
    data = []
    try:
        request = requests.get('https://slack.com/api/usergroups.list', 
                params = {'token': token.get_slack_token()},
                headers = {'Connection': 'close'} )
                
        data = request.json()
    
    except requests.exceptions.RequestException as e:
        print(e)
    
    return data
    

def get_usergroup_users_list(usergroup_id):
    """Returns a list with the ids of the users in a usergroup.
    
    Args:
        usergroup_id: The id of a Slack usergroup.
        
    Returns:
        Returns a list containing the ids of the users in the
        specified usergroup.
    """
    user_ids = []
    try:
        request = requests.get('https://slack.com/api/usergroups.users.list', 
                params = {'token': token.get_slack_token(),
                        'usergroup': usergroup_id },
                headers = {'Connection': 'close'})
        
        data = request.json()
        if data.get('ok'):
            user_ids = data.get('users')
        
    except Exception as e:
        print(e)
        
    return user_ids