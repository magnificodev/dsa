import unittest

# Method 1
# def sorted_squared(array):
#     return sorted([x**2 for x in array])
# ----------------------------------------------
# -> Space Complexity: O(n); 
# -> Time complexity O(nlogn)

# Method 2

# def sorted_squared(array):
#     i = 0
#     j = len(array) - 1
#     result = [0]*len(array)
#     for k in reversed(range(len(array))):
#         sq_i = array[i]**2
#         sq_j = array[j]**2
#         if sq_i > sq_j:
#             result[k] = sq_i
#             i += 1
#         else:
#             result[k] = sq_j
#             j -= 1
#     return result
# - Space complexity: O(n)
# - Time complexity: O(n)
# ----------------------------------------------

# Method 3
# def sorted_squared(array):
#     arrLen = len(array)
#     result = [0] * arrLen
    
#     for i in range(arrLen):
#         result[i] = array[i]**2
#     result.sort()
#     return result
# - Space complexity: 0(n)
# - Time complexity: O(n)
# ----------------------------------------------

# TEST CASES
class TestSquareAndSort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sorted_squared([]), [])

    def test_single_element_array(self):
        self.assertEqual(sorted_squared([2]), [4])

    def test_multiple_element_array(self):
        self.assertEqual(sorted_squared([1, 2, 3, 4]), [1, 4, 9, 16])
        self.assertEqual(sorted_squared([0, 1, 2, 3]), [0, 1, 4, 9])
        self.assertEqual(sorted_squared([5, 6, 7, 8]), [25, 36, 49, 64])

    def test_negative_numbers(self):
        self.assertEqual(sorted_squared([-3, -2, -1, 0]), [0, 1, 4, 9])
        self.assertEqual(sorted_squared([-5, -4, -3]), [9, 16, 25])

    def test_mixed_numbers(self):
        self.assertEqual(sorted_squared([-2, 0, 3, 5]), [0, 4, 9, 25])

if __name__ == '__main__':
    unittest.main()