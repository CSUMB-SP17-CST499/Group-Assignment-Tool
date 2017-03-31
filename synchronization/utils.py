from apis import slack


def get_salck_api_emails(data):
    """Function creates a 'get'request, in order to get all the emails from the slack team,
    by passing the token as a parameter for authentication.

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