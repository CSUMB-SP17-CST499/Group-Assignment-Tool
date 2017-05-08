import os, requests, json

def get_bugzilla_user_info(user):
    """Function used to obtain bugzilla user info

    Args:
        str: either a buzilla user's login name/email or id

    Returns:
        Returns id, name, real_name, email, can_login, and groups of user

    """
    
    request = requests.get('http://www.fruitfuldevelopment.com:8081/bugzilla/rest.cgi/user/' + user,
        params = {'Bugzilla_login': os.getenv("Bugzilla_login"),
        'Bugzilla_password': os.getenv('Bugzilla_password')}
        )
    return(request.json())
    
    
def get_bugzilla_group_info(group):
    """Function used to obtain bugzilla group info

    Args:
        str: either a buzilla group name or id

    Returns:
        Returns group details

    """
    
    request = requests.get('http://www.fruitfuldevelopment.com:8081/bugzilla/rest.cgi/group?names=' + group,
        params = {'Bugzilla_login': os.getenv("Bugzilla_login"),
        'Bugzilla_password': os.getenv('Bugzilla_password')
        }
        )
    return(request.json()["groups"][0])


def get_all_bugzilla_group_info():
    """Function used to obtain bugzilla user info

    Args:
        str: either a buzilla group name or id

    Returns:
        Returns id, name, real_name, email, can_login, and groups of user

    """
    
    request = requests.get('http://www.fruitfuldevelopment.com:8081/bugzilla/rest.cgi/group?',
        params = {'Bugzilla_login': os.getenv("Bugzilla_login"),
        'Bugzilla_password': os.getenv('Bugzilla_password')}
        )
    return(request.json())
    
def add_user_to_bugzilla_group(user):
    """Function used to obtain bugzilla user info

    Args:
        param1 (str): either a buzilla user's login name/email or id
        param2 (list: str) an array of either group names or ids
        

    Returns:
        Returns id, name, real_name, email, can_login, and groups of user

    """
    
    data = {}
    data['set'] = ['test']
    wrapData = {}
    wrapData['groups'] = data
    
    
    print(wrapData)
    # request = requests.put('http://www.fruitfuldevelopment.com:8081/bugzilla/rest.cgi/user/' + user,
    #     params = {'Bugzilla_login': os.getenv("Bugzilla_login"),
    #     'Bugzilla_password': os.getenv('Bugzilla_password'), 
    #     'groups': data}
    #     )
    # return(request.json())
 