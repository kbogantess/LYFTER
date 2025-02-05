import unittest
import pytest

def bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise TypeError("The input must be a list")

    for ext_i in range(len(list_to_sort)):
        swapped = False

        for i in range(0, len(list_to_sort) - 1):
            element = list_to_sort[i]
            next_element = list_to_sort[i + 1]

            if element > next_element:
                list_to_sort[i] = next_element
                list_to_sort[i + 1] = element
                swapped = True

        if not swapped:
            break

    return list_to_sort

class TestBubbleSort(unittest.TestCase):

    def test_small_list(self):
        self.assertEqual(bubble_sort([3, -3, 0, 1, -1, 2, -2]), [-3, -2, -1, 0, 1, 2, 3])

    def test_large_list(self):
        large_list = list(range(100, -1, -1))  #descending order
        sorted_large_list = list(range(101))  #ascending order
        self.assertEqual(bubble_sort(large_list), sorted_large_list)

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            bubble_sort("not a list")
            bubble_sort(12345)
            bubble_sort(None)

if __name__ == '__main__':
    unittest.main()



# PS C:\Users\50685\Desktop\VSCODE> & C:/Users/50685/AppData/Local/Programs/Python/Python313/python.exe c:/Users/50685/Desktop/VSCODE/Semana_16/bubble_sort_testing.py
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s

# OK
# PS C:\Users\50685\Desktop\VSCODE> 