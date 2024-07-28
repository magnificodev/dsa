# TESTING CODE

# import unittest
# import exercise


# class Evaluate(unittest.TestCase):
#     def test_monotonic_array(self):
#         # Test for increasing monotonic array
#         arr1 = [1, 2, 3, 4, 5]
#         self.assertTrue(exercise.monotonic_array(arr1), f"{arr1} should be monotonic")

#         # Test for decreasing monotonic array
#         arr2 = [5, 4, 3, 2, 1]
#         self.assertTrue(exercise.monotonic_array(arr2), f"{arr2} should be monotonic")

#         # Test for non-monotonic array
#         arr3 = [1, 3, 2, 4, 5]
#         self.assertFalse(
#             exercise.monotonic_array(arr3), f"{arr3} should not be monotonic"
#         )

#         # Test for empty array
#         arr4 = []
#         self.assertTrue(
#             exercise.monotonic_array(arr4), "Empty array should be monotonic"
#         )

#         # Test for array with a single element
#         arr5 = [1]
#         self.assertTrue(
#             exercise.monotonic_array(arr5),
#             "Array with a single element should be monotonic",
#         )


# if __name__ == "__main__":
#     unittest.main()

import unittest
import exercise

class Evaluate(unittest.TestCase):
    def test_increasing_monotonic_array(self):
        # Test for increasing monotonic array
        arr1 = [1, 2, 3, 4, 5]
        self.assertTrue(exercise.monotonic_array(arr1), f"Passed: {arr1} is monotonic")

    def test_decreasing_monotonic_array(self):
        # Test for decreasing monotonic array
        arr2 = [5, 4, 3, 2, 1]
        self.assertTrue(exercise.monotonic_array(arr2), f"Passed: {arr2} is monotonic")

    def test_non_monotonic_array(self):
        # Test for non-monotonic array
        arr3 = [1, 3, 2, 4, 5]
        self.assertFalse(exercise.monotonic_array(arr3), f"Passed: {arr3} is not monotonic")

    def test_empty_array(self):
        # Test for empty array
        arr4 = []
        self.assertTrue(exercise.monotonic_array(arr4), "Passed: Empty array is monotonic")

    def test_single_element_array(self):
        # Test for array with a single element
        arr5 = [1]
        self.assertTrue(exercise.monotonic_array(arr5), "Passed: Array with a single element is monotonic")

if __name__ == "__main__":
    unittest.main()
