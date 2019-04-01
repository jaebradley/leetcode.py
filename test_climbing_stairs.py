from unittest import TestCase

from climbing_stairs import Solution


class TestClimbingStairs(TestCase):
    def test_1_stair(self):
        self.assertEqual(Solution().climbStairs(1), 1)

    def test_2_stairs(self):
        self.assertEqual(Solution().climbStairs(2), 2)

    def test_3_stairs(self):
        self.assertEqual(Solution().climbStairs(3), 3)

    def test_4_stairs(self):
        self.assertEqual(Solution().climbStairs(4), 5)
