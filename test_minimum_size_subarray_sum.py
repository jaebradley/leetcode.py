from unittest import TestCase

from minimum_size_subarray_sum import Solution


class TestMinimumSizeSubarraySum(TestCase):
    def test_when_two_values_sum_directly_to_min(self):
        self.assertEqual(
            2,
            Solution().minSubArrayLen(
                7,
                [2, 3, 1, 2, 4, 3]
            )
        )

    def test_when_two_values_sum_to_value_greater_than_min(self):
        self.assertEqual(
            2,
            Solution().minSubArrayLen(
                6,
                [2, 3, 1, 2, 4, 3]
            )
        )

    def test_when_no_values_sum_to_value_greater_than_or_equal_to_min(self):
        self.assertEqual(
            0,
            Solution().minSubArrayLen(
                100,
                [1, 2, 3, 4]
            )
        )

    def test_when_all_values_sum_to_value_equal_to_min(self):
        self.assertEqual(
            4,
            Solution().minSubArrayLen(
                10,
                [1, 2, 3, 4]
            )
        )
