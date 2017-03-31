from apis import slack


def get_salck_api_emails(data):
    """Function parses all the emails from a dictionary containing all the Slack Team member's information

    Args:
        data: a dictionary containing all the information from each user in the Slack team

    Returns:
        Returns a list containing all the emails in the slack Team.

    """
    data = slack.get_user_list()
    users_emails = []
    member_amt = len(data["members"])
        
    for i in range(0, member_amt):
        profile_amt = len(data["members"][i]["profile"])
            
        profile = (data["members"][i])["profile"]
        if "email" in profile:
            users_emails.append(profile["email"])
            
    return users_emails
    
    
def get_salck_api_group_id(data):
    """Function parses all the group_ids from a dictionary containing all the Slack Team groups's information

    Args:
        data: a dictionary containing all the information from each group in the Slack team

    Returns:
        Returns a list containing all the group_ids in the slack Team.

    """
    group_ids = []
    group_amt = len(data["usergroups"])
        
    for group in data["usergroups"]:
        group_ids.append(group["id"])
    
            
    return group_ids