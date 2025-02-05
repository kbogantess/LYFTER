
def invert_string(string):
    return string[::-1]

import pytest
import unittest #"NUEVA BIBLIOTECA "

class TestInvertString(unittest.TestCase):
    
    def test_invert_string_word(self):
        self.assertEqual(invert_string("Hola"), "aloH")
    
    def test_invert_string_frase(self):
        self.assertEqual(invert_string("Hola mundo"), "odnum aloH")
    
    def test_invert_string_empty(self):
        self.assertEqual(invert_string(""), "")

if __name__ == '__main__':
    unittest.main()
