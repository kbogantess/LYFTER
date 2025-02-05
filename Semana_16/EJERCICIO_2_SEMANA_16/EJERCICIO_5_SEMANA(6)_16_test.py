def cont_mayus_minus(string):
    mayus = sum(1 for c in string if c.isupper())
    minus = sum(1 for c in string if c.islower())
    return f"There are {mayus} upper cases and {minus} lower cases"


import pytest
import unittest

class TestContMayusMinus(unittest.TestCase):

    def test_cont_mayus_minus_mixed(self):
        result = cont_mayus_minus("I love Nación Sushi")
        self.assertEqual(result, "There are 3 upper cases and 13 lower cases")
    
    def test_cont_mayus_minus_mayus(self):
        result = cont_mayus_minus("HELLO WORLD")
        self.assertEqual(result, "There are 10 upper cases and 0 lower cases")
    
    def test_cont_mayus_minus_minus(self):
        result = cont_mayus_minus("hello world")
        self.assertEqual(result, "There are 0 upper cases and 10 lower cases")

if __name__ == '__main__':
    unittest.main()
