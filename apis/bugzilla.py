import os, requests

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