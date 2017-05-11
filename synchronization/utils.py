from apis import slack
from db import query
from db.models import Group, Employee

    
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
    slack_ids = {usergroup.slack_id for usergroup in slack_usergroups}
    db_ids = {group.app_group_id for group in groups}
    missing_ids = slack_ids - db_ids
    
    return missing_ids
    
    
def get_missing_user_ids(slack_users, users):
    """Returns the ids of Slack users that are not already in the database.
    
    Args:
        slack_users: A dictionary with a list of users from slack.
    """
    slack_ids = {user.slack_id for user in slack_users}
    db_ids = {user.slack_id for user in users}
    missing_ids = slack_ids - db_ids
    
    return missing_ids