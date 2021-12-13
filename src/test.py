import unittest
import lamda_function
import calculateAnds

class Test(unittest.TestCase):
    def setup(self): 
          lamda_function.app.config['TESTING'] = True 
          self.app = lamda_function.app.test_client() 
    
    def test_count_and(self):
        self.assertEqual(calculateAnds.calculateAnds('and'), 1)

    def test_average_empty_string(self):
        self.assertEqual(calculateAnds.calculateAnds(''), 0)
