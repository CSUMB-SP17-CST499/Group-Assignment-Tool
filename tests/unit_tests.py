import unittest
from apis import slack

class testSlackFunctions(unittest.TestCase):

    def test_self(self):
        result = ''.split()
        self.assertEquals(result, [])
        
    def test_get_user_groups(self):
        result = slack.get_user_groups()
        self.assertIsNotNone(result)
        print(result)
        
    def test_get_users(self):
        groups = slack.get_user_groups()
        for x in groups:
            result = slack.get_users(x)
            self.assertIsNotNone(result)
            print(result)
            
    def test_get_user_names(self):
        groups = slack.get_user_groups()
        result = slack.get_users(groups[0])
        # userName = slack.get_user_names(result)
        # print(userName)
            
    def test_update_employees(self):
        slack.update_employees()
    
    def test_create_group(self):
        slack.create_group()


if __name__ == '__main__':
    unittest.main()