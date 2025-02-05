
def add_list(numbers):
    return sum(numbers)

###################################################################################

import pytest
import unittest #OTRA BIBLIOTECA

class Test_add_list(unittest.TestCase):
    
    def test_add_positive_list(self):
        self.assertEqual(add_list([4, 6, 2, 29]), 41)
    
    def test_add_negative_list(self):
        self.assertEqual(add_list([-1, -2, -3, -4]), -10)
    
    def test_add_mixed_list(self):
        self.assertEqual(add_list([-1, 2, -3, 4]), 2)

if __name__ == '__main__':
    unittest.main()
