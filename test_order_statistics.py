import unittest
import re # Import re for escaping
from order_statistics import find_kth_largest, find_min_max

class TestFindKthLargest(unittest.TestCase):

    def test_various_arrays_and_k_values(self):
        self.assertEqual(find_kth_largest([3, 1, 4, 1, 5, 9, 2, 6], 1), 9) # 1st largest
        self.assertEqual(find_kth_largest([3, 1, 4, 1, 5, 9, 2, 6], 3), 5) # 3rd largest
        self.assertEqual(find_kth_largest([3, 1, 4, 1, 5, 9, 2, 6], 8), 1) # 8th largest (smallest)
        self.assertEqual(find_kth_largest([10, 4, 5, 8, 6, 11, 26], 2), 11) # 2nd largest
        self.assertEqual(find_kth_largest([-1, -5, -2, -8], 1), -1) # 1st largest (negative numbers)
        self.assertEqual(find_kth_largest([-1, -5, -2, -8], 4), -8) # 4th largest (smallest negative)
        self.assertEqual(find_kth_largest([5, 5, 5, 5], 2), 5) # Duplicates
        self.assertEqual(find_kth_largest([1, 2, 3, 4, 5, 6], 3), 4) # Median-ish
        self.assertEqual(find_kth_largest([6, 5, 4, 3, 2, 1], 3), 4) # Reverse sorted

    def test_k_equals_one(self):
        self.assertEqual(find_kth_largest([7, 2, 9, 1, 5], 1), 9)
        self.assertEqual(find_kth_largest([-3, -1, -5], 1), -1)

    def test_k_equals_length(self):
        self.assertEqual(find_kth_largest([7, 2, 9, 1, 5], 5), 1) # Smallest element
        self.assertEqual(find_kth_largest([-3, -1, -5], 3), -5) # Smallest element

    def test_invalid_k_too_small(self):
        # Escape the period for literal matching.
        with self.assertRaisesRegex(ValueError, re.escape("k must be between 1 and 3 (inclusive), but got 0.")):
            find_kth_largest([1, 2, 3], 0)
        with self.assertRaisesRegex(ValueError, re.escape("k must be between 1 and 3 (inclusive), but got -1.")):
            find_kth_largest([1, 2, 3], -1)

    def test_invalid_k_too_large(self):
        with self.assertRaisesRegex(ValueError, re.escape("k must be between 1 and 3 (inclusive), but got 4.")):
            find_kth_largest([1, 2, 3], 4)

    def test_empty_array(self):
        # This message does not have regex special characters other than potentially '.'
        with self.assertRaisesRegex(ValueError, re.escape("Input array cannot be empty.")):
            find_kth_largest([], 1)

    def test_single_element_array(self):
        self.assertEqual(find_kth_largest([42], 1), 42)
        with self.assertRaisesRegex(ValueError, re.escape("k must be between 1 and 1 (inclusive), but got 2.")):
            find_kth_largest([42], 2)
        with self.assertRaisesRegex(ValueError, re.escape("k must be between 1 and 1 (inclusive), but got 0.")):
            find_kth_largest([42], 0)

class TestFindMinMax(unittest.TestCase):

    def test_various_arrays(self):
        self.assertEqual(find_min_max([3, 1, 4, 1, 5, 9, 2, 6]), (1, 9))
        self.assertEqual(find_min_max([10, 4, 5, 8, 6, 11, 26]), (4, 26))
        self.assertEqual(find_min_max([-1, -5, -2, -8]), (-8, -1))
        self.assertEqual(find_min_max([5, 5, 5, 5]), (5, 5)) # Duplicates
        self.assertEqual(find_min_max([1, 2, 3, 4, 5, 6]), (1, 6))
        self.assertEqual(find_min_max([6, 5, 4, 3, 2, 1]), (1, 6)) # Reverse sorted
        self.assertEqual(find_min_max([0, 0, 0, -1, 1]), (-1, 1)) # Mixed with zero

    def test_single_element_array(self):
        self.assertEqual(find_min_max([42]), (42, 42))
        self.assertEqual(find_min_max([-7]), (-7, -7))

    def test_two_elements_sorted(self):
        self.assertEqual(find_min_max([1, 5]), (1, 5))
        self.assertEqual(find_min_max([-5, -1]), (-5, -1))

    def test_two_elements_unsorted(self):
        self.assertEqual(find_min_max([5, 1]), (1, 5))
        self.assertEqual(find_min_max([-1, -5]), (-5, -1))

    def test_empty_array(self):
        with self.assertRaisesRegex(ValueError, re.escape("Input array cannot be empty.")):
            find_min_max([])

    def test_return_type_and_values(self):
        arr = [3, 1, 7, 2, 8]
        result = find_min_max(arr)
        self.assertIsInstance(result, tuple, "Should return a tuple")
        self.assertEqual(len(result), 2, "Tuple should have two elements")
        self.assertEqual(result[0], 1, "Min value is incorrect")
        self.assertEqual(result[1], 8, "Max value is incorrect")
        self.assertEqual(result, (min(arr), max(arr)), "Result should match min() and max()")

if __name__ == '__main__':
    unittest.main()
