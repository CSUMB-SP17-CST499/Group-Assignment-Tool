from apis import slack
from db import query
from db.models import Group, Employee


def parse_emails_from_slack_users(data):
    """Parses the the emails from a dictionary with Slack user information.

    Args:
        data: a dictionary containing all the information from each user in the Slack team

    Returns:
        Returns a list containing all  emails from the slack team.
    """            
    emails = []
    for user in data["members"]:
        if "profile" in user and "email" in user["profile"]:
            emails.append(user["profile"]["email"])
            
    return emails
    
    
def parse_ids_from_slack_usergroups(data):
    """Parses the usergroup ids from a dictionary with Slack usergroup data.

    Args:
        data: a dictionary containing information for each group 
            in the Slack team.

    Returns:
        Returns a list containing all the group ids in the Slack team.
    """
    return [usergroup.get("id") for usergroup in data.get("usergroups")]
    
    
def parse_ids_from_slack_users(data):
    """Parses the user ids from a dictionary with Slack user data.
    
    Args:
        data: A dictionary containing information for each user 
            in the Slack team.
        
    Returns:
        Returns a list containing all the user ids in the Slack team.
    """
    return [member.get("id") for member in data.get("members")]
    

def parse_user_ids_from_slack_usergroup(data):
    """Parses the user ids from a dictionary with an updated Slack usergroup.
    
    Args:
        data: A dictionary containing information for the
            updated usergroup from Slack.
            
    Returns:
        Returns a list of the user ids from a Slack usergroup.
    """
    return [user_id for user_id in data.get('usergroup').get('users')]
    
    
def get_missing_group_ids(slack_usergroups, groups):
    """Returns the ids of Slack usergroups that are not already in the database.
    
    Args:
        slack_usergroups: A dictionary with data from the Slack 
            usergroups.list endpoint.
        groups: A list of Group instances that are from Slack.
    
    Returns:
        Returns a list of ids belonging to Slack usergroups 
        that are not in the database.
    """
    slack_ids = set(parse_ids_from_slack_usergroups(slack_usergroups) )
    db_ids = {group.app_group_id for group in groups}
    missing_ids = slack_ids - db_ids
    
    return missing_ids
    
    
def get_missing_user_ids(slack_users, users):
    """Returns the ids of Slack users that are not already in the database.
    
    Args:
        slack_users: A dictionary with a list of users from slack.
    """
    slack_ids = set(parse_ids_from_slack_users(slack_users) )
    db_ids = {user.slack_id for user in users}
    missing_ids = slack_ids - db_ids
    
    return missing_ids