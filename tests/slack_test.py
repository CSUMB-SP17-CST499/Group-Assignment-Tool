import unittest
from apis import slack
from apis import token

class TestSlackConnection(unittest.TestCase):
    
    
    def test_get_slack_token(self):
        slack_token = token.get_slack_token()
        self.assertIsNotNone(slack_token)
    
    
    def test_client_init(self):
        slack_token = token.get_slack_token()
        client = slack.SlackClient(slack_token)
        self.assertIsNotNone(client)
        

if __name__ == '__main__':
    unittest.main()