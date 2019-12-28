from unittest import TestCase

from daily_temperatures import Solution


class TestDailyTemperatures(TestCase):
    def test_single_temperature(self):
        wait_values = Solution().dailyTemperatures([1])
        self.assertListEqual(wait_values, [0])

    def test_two_increasing_temperatures(self):
        wait_values = Solution().dailyTemperatures([1, 2])
        self.assertListEqual(wait_values, [1, 0])

    def test_two_decreasing_temperatures(self):
        wait_values = Solution().dailyTemperatures([2, 1])
        self.assertListEqual(wait_values, [0, 0])

    def test_two_equal_temperatures(self):
        wait_values = Solution().dailyTemperatures([1, 1])
        self.assertListEqual(wait_values, [0, 0])

    def test_three_temperatures_with_largest_first_smallest_second_and_middle_last(self):
        wait_values = Solution().dailyTemperatures([3, 1, 2])
        self.assertListEqual(wait_values, [0, 1, 0])

    def test_three_temperatures_with_middle_first_smallest_middle_and_largest_last(self):
        wait_values = Solution().dailyTemperatures([2, 1, 3])
        self.assertListEqual(wait_values, [2, 1, 0])
