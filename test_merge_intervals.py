from unittest import TestCase

from merge_intervals import Solution


class TestMergeIntervals(TestCase):
    def test_two_overlapping_intervals(self):
        self.assertEqual(Solution().merge([[1, 3], [2, 6]]), [[1, 6]])

    def test_two_overlapping_intervals_that_share_an_endpoint(self):
        self.assertEqual(Solution().merge([[1, 4], [4, 5]]), [[1, 5]])
