from unittest import TestCase

from combination_sum_four import Solution


class TestCombinationSumFour(TestCase):
    def test_four_using_one_two_and_three(self):
        self.assertEqual(Solution().combinationSum4([1, 2, 3], 4), 7)

    def test_empty_nums(self):
        self.assertEqual(Solution().combinationSum4([], 1), 0)

    def test_nums_greater_than_target(self):
        self.assertEqual(Solution().combinationSum4([9], 3), 0)

    def test(self):
        self.assertEqual(Solution().combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10), 9)
