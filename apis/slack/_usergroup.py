class UserGroup():
    
    def __init__(self, slack_id, name, users = []):
        self.slack_id = slack_id
        self.name = name
        self.users = users