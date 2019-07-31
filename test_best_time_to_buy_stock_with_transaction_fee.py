from unittest import TestCase


from best_time_to_buy_stock_with_transaction_fee import Solution


class TestMultipleTrades(TestCase):
    def test_two_trades(self):
        self.assertEqual(
            8,
            Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
        )


class TestSingleTrade(TestCase):
    def test_single_trade_at_beginning_to_end(self):
        self.assertEqual(
            8,
            Solution().maxProfit([1, 2, 3, 4, 5, 10], 1)
        )

    def test_single_trade_beginning_and_next_period(self):
        self.assertEqual(
            8,
            Solution().maxProfit([1, 11, 1, 1, 1], 2)
        )

    def test_single_trade_last_and_penultimate(self):
        self.assertEqual(
            9,
            Solution().maxProfit([0, 0, 0, 0, 1, 12], 3)
        )

    def test_single_trade_middle(self):
        self.assertEqual(
            9,
            Solution().maxProfit([0, 0, 1, 13, 0, 0, 0], 4)
        )


class TestZeroTrades(TestCase):
    def test_zero_trades_when_decreasing(self):
        self.assertEqual(
            0,
            Solution().maxProfit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1)
        )
