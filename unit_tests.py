import unittest
from apis import slack

class testSlackFunctions(unittest.TestCase):

    def test_self(self):
        result = ''.split()
        self.assertEquals(result, [])
        
    def test_get_user_groups(self):
        result = slack.get_user_groups()
        self.assertIsNotNone(result)
        
    def test_get_user_group_id(self):
        result = slack.get_user_group_ids()
        self.assertIsNotNone(result)
        print("Result of get user group ID XOXOXOXOXOXOXOXOXOX ")
        print(result)
        
    def test_get_users(self):
        groups = slack.get_user_groups()
        for x in groups:
            result = slack.get_users(x)
            self.assertIsNotNone(result)
            # print(result)
            
    def test_get_user_names(self):
        groups = slack.get_user_groups()
        result = slack.get_users(groups[0])
        # userName = slack.get_user_names(result)
        # print(userName)
            
    def test_update_employees(self):
        group_ids = slack.get_user_group_ids()
        print("These are group IDs")
        print(group_ids)
        groups = slack.get_user_groups()
        first_group_id = group_ids[0]
        first_group_name = groups[0]
        user_ids = slack.get_users(first_group_name)
        first_user_id = user_ids[0]
        print("This is the first group")
        print(first_group_id)
        print("These are user_ids in the first group")
        print(user_ids)
        print("The first user_id in that group is:")
        print(first_user_id)
        print("Removing the first user from the first group....")
        user_ids.remove(first_user_id)
        slack.update_employees(user_ids, first_group_id)
        updated_user_list = slack.get_users(first_group_name)
        
            # THE LIST BEING PASSED IS NOT THE RESULTING LIST. FAILING TEST CASE
        self.assertEquals(user_ids, updated_user_list)
        print("This is the updated userlist for the firt group with the user removed: ")
        print(updated_user_list)
        print("Adding the first user back to the first group....")
        user_ids.append(first_user_id)
        slack.update_employees(user_ids, first_group_id)
        updated_user_list = slack.get_users(first_group_id)
        print("This is the updated userlist for the firt group: ")
        print(updated_user_list)
        

        
    
    def test_create_group(self):
        slack.create_group()


if __name__ == '__main__':
    unittest.main()