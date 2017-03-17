import requests
from apis import token

  
def get_user_groups():
    """Function creates a 'get'reques by passing the token as a parameter for authentication.

    Args:
        none

    Returns:
        Returns a list containing Slack group names.

    """
    request = requests.get('https://slack.com/api/usergroups.list', params = {'token': token.get_slack_token()})
    data = request.json()
    names = []
    size = len(data)
    for i in range (0, size):
       names.append(data['usergroups'][i]['name'])
    return names
    
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
        request = requests.get('https://slack.com/api/usergroups.list', params = {'token': token.get_slack_token(), 'include_users': "true"})
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
            request = requests.get('https://slack.com/api/users.info', params = {'token': token.get_slack_token(), 'user': id})
            data = request.json()
            users_names.append(data['user']['name'])
            
        except requests.exceptions.RequestException as e:
            print(e)
            
    return users_names
    
def update_employees():
    pass

def create_group():
    pass