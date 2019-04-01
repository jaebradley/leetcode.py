from unittest import TestCase

from search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(TestCase):
    def test_0_when_first_element_is_target(self):
        self.assertEqual(Solution().search([1, 2, 3, 4, 5, 6, 7], 1), 0)

    def test_end_index_last_element_is_target(self):
        self.assertEqual(Solution().search([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_middle_index_is_target(self):
        self.assertEqual(Solution().search([1, 2, 3, 4, 5, 6, 7], 4), 3)

    def test_0_when_first_element_is_target_when_rotated(self):
        self.assertEqual(Solution().search([5, 6, 7, 1, 2, 3, 4], 5), 0)

    def test_two_element_descending_second_element(self):
        self.assertEqual(Solution().search([2, 1], 1), 1)

    def test_two_element_descending_first_element(self):
        self.assertEqual(Solution().search([2, 1], 2), 0)

    def test_two_element_ascending_first_element(self):
        self.assertEqual(Solution().search([1, 2], 1), 0)

    def test_two_element_ascending_second_element(self):
        self.assertEqual(Solution().search([1, 2], 2), 1)

    def test_unable_to_find_element(self):
        self.assertEqual(Solution().search([1, 2, 3, 4, 5, 6], 7), -1)

    def test_target_element_is_right_of_pivot(self):
        self.assertEqual(Solution().search([4, 5, 6, 7, 0, 1, 2], 0), 4)
