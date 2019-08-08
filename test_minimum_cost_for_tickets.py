from unittest import TestCase

from minimum_cost_for_tickets import Solution


class TestMinimumCostForTickets(TestCase):
    def test_multiple_days(self):
        self.assertEqual(11, Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))

    def test_another(self):
        self.assertEqual(17, Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
