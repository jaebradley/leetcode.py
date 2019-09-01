from unittest import TestCase

from min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs(TestCase):
    def test_start_on_second_step(self):
        self.assertEqual(15, Solution().minCostClimbingStairs([10, 15, 20]))

    def test_high_and_low_cost_steps(self):
        self.assertEqual(6, Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

    def test_start_value_and_end_value(self):
        self.assertEqual(0, Solution().minCostClimbingStairs([1, 0, 0, 1]))