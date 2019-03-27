from unittest import TestCase

from maximum_subarray import Solution


class TestMaximumSubarray(TestCase):
    def test_positives_amongst_negatives(self):
        self.assertEqual(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_monotonically_increasing(self):
        self.assertEqual(Solution().maxSubArray([0, 1, 2, 3, 4, 5, 6]), 21)

    def test_monotonically_decreasing(self):
        self.assertEqual(Solution().maxSubArray([6, 5, 4, 3, 2, 1, 0]), 21)

    def test_positives_then_negatives(self):
        self.assertEqual(Solution().maxSubArray([1, 2, 3, 4, -4, -3, -2, -1]), 10)

    def test_negatives(self):
        self.assertEqual(Solution().maxSubArray([-6, -5, -4, -3, -2, -1]), -1)
