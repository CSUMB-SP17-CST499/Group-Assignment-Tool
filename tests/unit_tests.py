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
        
    def test_get_users(self):
        groups = slack.get_user_groups()
        for x in groups:
            result = slack.get_users(x)
            self.assertIsNotNone(result)
            
            
    def test_get_user_names(self):
        pass

            
    def test_update_employees(self):
        group_names = slack.get_user_groups()
        first_group_name = group_names[0]
        group_ids = slack.get_user_group_ids()
        print("These are group IDs")
        print(group_ids)
        groups = slack.get_user_groups()
        first_group_id = group_ids[0]
        
        user_ids = slack.get_user_ids(first_group_id)
        print("These are IDs of the users in the group")
        print(user_ids)
        
        first_user_id = user_ids[0]
        print("This is the first user id")
        print(first_user_id)
        
        print("Testing local list: before remove:")
        print(user_ids)
        user_ids.remove(first_user_id)
        print("Testing local list: after:")
        print(user_ids)
        
        updated_user_list = slack.get_users(first_group_name)
        print("Testing slack list: before remove:")
        print(updated_user_list)
        
        # Call the function to update the userlist
        comma_separated_user_ids = ",".join(user_ids)
        slack.update_employees(comma_separated_user_ids, first_group_id)
        
        updated_user_list = slack.get_users(first_group_name)
        print("Testing slack list: after remove:")
        print(updated_user_list)
        
        user_ids.append(first_user_id)
        comma_separated_user_ids = ",".join(user_ids)
        slack.update_employees(comma_separated_user_ids, first_group_id)
        
        updated_user_list = slack.get_users(first_group_name)
        print("Testing slack list: after adding user back:")
        print(updated_user_list)
        
    
    def test_create_group(self):
        slack.create_group()


if __name__ == '__main__':
    unittest.main()