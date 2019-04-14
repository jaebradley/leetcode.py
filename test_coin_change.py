from unittest import TestCase

from coin_change import Solution


class TestCoinChange(TestCase):
    def test_multiple_of_one_coin(self):
        self.assertEqual(Solution().coinChange([1, 2, 5], 11), 3)

    def test_zero(self):
        self.assertEqual(Solution().coinChange([1, 2, 3], 0), 0)

    def test_unreachable_value(self):
        self.assertEqual(Solution().coinChange([2], 3), -1)

    def test_reachable_value_that_encounters_unreachable_value(self):
        self.assertEqual(Solution().coinChange([2], 4), 2)
