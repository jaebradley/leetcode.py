from unittest import TestCase

from find_minimum_in_rotated_sorted_array import Solution


class TestFindMinimumInRotatedSortedArray(TestCase):
    def test_first_element_is_minimum(self):
        self.assertEqual(Solution().findMin([0, 1, 2, 3, 4, 5]), 0)

    def test_left_of_pivot_element_is_minimum(self):
        self.assertEqual(Solution().findMin([6, 7, 0, 1, 2, 3, 4]), 0)

    def test_right_of_pivot_element_is_minimum(self):
        self.assertEqual(Solution().findMin([3, 4, 5, 7, 0, 1, 2]), 0)

    def test_last_element_is_minimum(self):
        self.assertEqual(Solution().findMin([1, 2, 3, 4, 5, 6, 0]), 0)

    def test_middle_element_is_minimum(self):
        self.assertEqual(Solution().findMin([4, 5, 6, 0, 1, 2, 3]), 0)

    def test_two_values(self):
        self.assertEqual(Solution().findMin([2, 1]), 1)
