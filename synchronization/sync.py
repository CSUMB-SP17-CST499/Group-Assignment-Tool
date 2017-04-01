from apis import slack
from synchronization import utils
from db import query
from db.models import Group


def sync_slack_users():
    """Function adds all the users from the Slack team that are not in the database to the database

    Args:
        none

    Returns:
        Retus a list containing all the emails in the slack Team.

    """
    
    data = slack.get_user_list()
    api_emails = utils.get_salck_api_emails(data)
    db_emails = []
    missing_users = []
    
    for db_user in query.get_all_employees():
        db_emails.append(db_user.email)
        
    for api_user in api_emails:
        if api_user not in db_emails:
            missing_users.append(api_user)
    
    users_emails = []
    member_amt = len(data["members"])
    
    for i in range(0, member_amt):
        first_name = ""
        last_name = ""
        profile_amt = len(data["members"][i]["profile"])
        profile = (data["members"][i])["profile"]
        
        for email in missing_users:
            if "email" in profile:
                if email == profile["email"]:
                    if "first_name" in profile and "last_name" in profile:
                        first_name = profile["first_name"]
                        last_name = profile["last_name"]
                        users_emails.append(profile["last_name"])
                        employee = query.Employee(email, first_name, last_name)
                        query.add_employee(employee)
    
  
def sync_slack_groups():
    """Function adds all the groups from the Slack team that are not in the database to the database

    Args:
        none

    Returns:
        Retus a list containing all the group_ids in the slack Team.

    """
    data = slack.get_user_groups_list()
    api_ids = utils.get_salck_api_group_id(data)
    db_ids = []
    missing_ids = []
    
    
    for db_id in query.get_all_groups():
        db_ids.append(db_id.group_id)
        
    for api_id in api_ids:
        if api_id not in db_ids:
            missing_ids.append(api_id)
    group_ids = []
    group_amt = len(data["usergroups"])
        
    for group in data["usergroups"]:
        name = ""
        for id in missing_ids:
            if "id" in group:
                if group["id"] == id:
                    if "name" in group:
                        name = group["name"]
                        group_obj = Group(None, name, 1, group["id"])
                        query.update_group(group_obj)
    
    
