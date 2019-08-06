from unittest import TestCase

from trapping_rain_water import Solution


class TestTrappingWater(TestCase):
    def test_trap_water(self):
        self.assertEqual(
            6,
            Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        )

    def test_trap_water_same_height(self):
        self.assertEqual(
            0,
            Solution().trap([1, 1, 1, 1, 1, 1])
        )

    def test_submerged_brick(self):
        self.assertEqual(
            13,
            Solution().trap([5, 0, 2, 0, 5])
        )

    def test_high_low(self):
        self.assertEqual(
            4,
            Solution().trap([20, 0, 4])
        )
