import unittest
from db import query

class testQueryFunctions(unittest.TestCase):

    def test_self(self):
        result = ''.split()
        self.assertEqual(result, [])
        
if __name__ == '__main__':
    unittest.main()