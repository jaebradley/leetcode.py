from unittest import TestCase

from best_time_to_buy_sell_stock import Solution


class TestBestTimeToBuySellStock(TestCase):
    def test_monotonically_increasing(self):
        self.assertEqual(Solution().maxProfit([1, 2, 3]), 2)

    def test_monotonically_decreasing(self):
        self.assertEqual(Solution().maxProfit([3, 2, 1]), 0)

    def test_valley(self):
        self.assertEqual(Solution().maxProfit([5, 4, 3, 2, 1, 2, 3, 4, 5]), 4)

    def test_two_valleys(self):
        self.assertEqual(Solution().maxProfit([5, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 5]), 4)
