from apis import slack
from apis import token
from synchronization import utils
from db import query
from db.models import Group, Employee
from typing import List


def sync_slack_users():
    """Adds users from Slack into the database if they do not already exist.
    
    When a user with a specific email already exists, but they do not have a 
    Slack user id, then the user's Slack id will be added if it exists.
    """
    client = slack.SlackClient(token.get_slack_token())
    slack_users = client.get_users_list()
    users = query.get_all_employees()
    missing_ids = utils.get_missing_user_ids(slack_users, users)
    
    for user in slack_users:
        if user.slack_id in missing_ids:
            employee = query.get_employee_by_email(user.email)
            
            if employee:
                employee.slack_id = user.slack_id
            else:
                employee = Employee(first_name = user.first_name, 
                        last_name = user.last_name,
                        email = user.email,
                        slack_id = user.slack_id)
            query.update_employee(employee)
            
  
def sync_slack_groups():
    """Adds groups from Slack into the database, if they do not already exist.
    """
    client = slack.SlackClient(token.get_slack_token())
    slack_usergroups = client.get_usergroups_list()
    groups = query.get_slack_groups()
    missing_ids = utils.get_missing_group_ids(slack_usergroups, groups)
    
    for usergroup in slack_usergroups:
        if usergroup.slack_id in missing_ids:
            name = usergroup.name
            slack_group_id = usergroup.slack_id
            
            if name and slack_group_id:
                group = Group(name, slack_group_id, 1)
                query.add_group(group)
                
                        
def add_to_slack_group(group: Group, employees: List[Employee]) -> List[str]:
    """Adds the passed in employee to the passed in group in the appropriate app.
    
    Args:
        group: A group from one of the integrated apps.
        employees: A list of employees that represent users 
            in Slack or Bugzilla.
        
    Returns:
        Returns a set of ids of the employees added to the group. An empty
        list is retured if no employees are added.
    """
    group_id = group.app_group_id
    user_ids = set(slack.get_usergroup_users_list(group_id))
    employee_ids = {employee.slack_id for employee in employees 
            if employee.slack_id and employee.slack_id}
    new_ids = employee_ids - user_ids
    encoded_ids = ','.join(user_ids.union(new_ids))

    data = slack.update_usergroup_users(group_id, encoded_ids)
    updated_ids = {}
    if data and data.get('ok'):
        user_ids = set(utils.parse_user_ids_from_slack_usergroup(data))
        updated_ids = user_ids.intersection(new_ids)
    
    return updated_ids


def remove_from_slack_group(group: Group, employees: List[Employee]) -> List[str]:
    """Removes the passed in employees from the passed in Slack group.
                                                
    Args:
        group: A group from one of the slack app.
        employees: A list of employees that represent users 
            in Slack or Bugzilla.
        
    Returns:
        Returns a set of ids of the employees removed to the group. An empty
        list is retured if no employees are removed.
    """
    group_id = group.app_group_id
    user_ids = set(slack.get_usergroup_users_list(group_id))
    employee_ids = {employee.slack_id for employee in employees 
            if employee.slack_id and employee.slack_id}

    encoded_ids = ','.join(user_ids - employee_ids)
    data = slack.update_usergroup_users(group_id, encoded_ids)
    updated_ids = {}
    if data and data.get('ok'):
        user_ids = set(utils.parse_user_ids_from_slack_usergroup(data))
        updated_ids = employee_ids - user_ids
    
    return updated_ids


def create_employee_from_slack_profile(profile) -> Employee:
    """Returns an instance of Employee with the information from a Slack profile.
    
    Args:
        profile: A dictionary that contains Slack profile info for a user.
        
    Returns:
        Returns an Employee with the profile info.
    """
    return Employee(profile.get("email"), 
            profile.get("first_name"), 
            profile.get("last_name")
        )
        