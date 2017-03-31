from apis import slack
from synchronization import utils
from db import query


def sync_slack_users():
    """Function adds all the users from the Slack team that are not in the database 

    Args:
        data: a dictionary containing all the information from each user in the slack team

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
    
  
    
    
