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
    for i in range (0, 2):
       names.append(data['usergroups'][i]['name'])
    return names
    
def update_employees():
    pass

def create_group():
    pass