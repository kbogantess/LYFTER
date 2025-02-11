import unittest
import pytest

def bubble_sort(list_to_sort):

    if not isinstance(list_to_sort, list):

        raise TypeError("The input must be a list")

    n = len(list_to_sort)
    
    for ext_i in range(n):

        swapped = False

        for i in range(0, n - ext_i - 1):  

            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swapped = True

        if not swapped:
            break

    return list_to_sort


class TestBubbleSort(unittest.TestCase):

    def test_small_list(self):

        self.assertEqual(bubble_sort([3, -3, 0, 1, -1, 2, -2]), [-3, -2, -1, 0, 1, 2, 3])

    def test_large_list(self):
        large_list = list(range(100, -1, -1))  # Descending 
        sorted_large_list = list(range(101))  # Ascending 

        self.assertEqual(bubble_sort(large_list), sorted_large_list)

    def test_empty_list(self):

        self.assertEqual(bubble_sort([]), [])

    
    def test_invalid_input_string(self):

        with self.assertRaises(TypeError):

            bubble_sort("not a list")

    def test_invalid_input_integer(self):

        with self.assertRaises(TypeError):

            bubble_sort(12345)

    def test_invalid_input_none(self):

        with self.assertRaises(TypeError):

            bubble_sort(None)


if __name__ == '__main__':

    unittest.main()



# PS C:\Users\50685\Desktop\VSCODE> & C:/Users/50685/AppData/Local/Programs/Python/Python313/python.exe c:/Users/50685/Desktop/VSCODE/Semana_16/bubble_sort_testing.py
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s

# OK
# PS C:\Users\50685\Desktop\VSCODE> 


# Después del cambio:

# PS C:\Users\XPC\Downloads\LYFTER> & C:/Users/XPC/AppData/Local/Programs/Python/Python313/python.exe c:/Users/XPC/Downloads/LYFTER/Semana_16/EJERCICIO_1_SEMANA_16/bubble_sort_testing.py
# ......
# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s

# OK
# PS C:\Users\XPC\Downloads\LYFTER>