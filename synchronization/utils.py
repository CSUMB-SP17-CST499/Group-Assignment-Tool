from apis import slack


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
    
    
def parse_ids_from_slack_usergroup(data):
    """Parses the usergroup ids from a dictionary with Slack usergroup data.

    Args:
        data: a dictionary containing information for each group 
            in the Slack team.

    Returns:
        Returns a list containing all the group_ids in the slack Team.
    """
    return [usergroup["id"] for usergroup in data["usergroups"]]