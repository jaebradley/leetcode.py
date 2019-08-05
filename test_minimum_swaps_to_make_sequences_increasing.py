from unittest import TestCase

from minimum_swaps_to_make_sequences_increasing import Solution


class TestSingleSwap(TestCase):
    def test_swap_where_not_increasing(self):
        self.assertEqual(1, Solution().minSwap([1, 3, 5, 4], [1, 2, 3, 7]))

    def test_swap_before_increasing(self):
        self.assertEqual(1, Solution().minSwap([0, 3, 2, 10], [0, 1, 11, 20]))


class TestNoSwap(TestCase):
    def test_two_monotonically_increasing_have_0_swaps(self):
        self.assertEqual(0, Solution().minSwap([0, 1, 2, 3], [10, 11, 12, 13]))


class TestMultipleSwaps(TestCase):
    def test_multiple_swaps(self):
        self.assertEqual(2, Solution().minSwap([10, 11, 6, 7], [4, 5, 12, 13]))
