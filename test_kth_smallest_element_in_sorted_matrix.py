from unittest import TestCase

from kth_smallest_element_in_sorted_matrix import Solution


class TestKthSmallestElementInSortedMatrix(TestCase):
    def test_duplicate_element(self):
        self.assertEqual(
            13,
            Solution().kthSmallest([
               [1,  5,  9],
               [10, 11, 13],
               [12, 13, 15]
            ], 8))
