from unittest import TestCase

from three_sum import Solution


class TestThreeSum(TestCase):
    def test_duplicate_solution(self):
        self.assertEqual(Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_three_zeroes(self):
        self.assertEqual(Solution().threeSum([0, 0, 0]), [[0, 0, 0]])
