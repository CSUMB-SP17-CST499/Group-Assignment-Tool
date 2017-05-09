import os, requests

def get_slack_token():
    """Function used to obtain the Slack token

    Args:
        none

    Returns:
        Returns the enviroment variable containig the value of the Slack token used for authentication.

    """
    return (os.getenv("SLACK_TOKEN"))
    