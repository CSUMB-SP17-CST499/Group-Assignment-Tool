from apis import slack





def get_salck_api_emails():
    
    data = slack.get_user_list()
    users_emails = []
    member_amt = len(data["members"])
        
    for i in range(0, member_amt):
        profile_amt = len(data["members"][i]["profile"])
            
        profile = (data["members"][i])["profile"]
        if "email" in profile:
            users_emails.append(profile["email"])
            
    return users_emails
