import unittest
import app

class RenderTests(unittest.TestCase):
    render_templates = False
    
    def test_empty_string(self):
        result = ''.split()
        self.assertEquals(result, [])

if __name__ == '__main__':
    unittest.main()