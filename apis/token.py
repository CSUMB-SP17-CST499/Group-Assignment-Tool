import os

def get_slack_token():
    """
       Returns the enviroment variable containig the value of the token used for authentication.
    """
    return (os.getenv("SLACK_TOKEN"))
    
    