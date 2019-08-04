from unittest import TestCase

from partition_to_k_equal_sum_subsets import Solution


class TestPartitionSingleSubset(TestCase):
    def test_can_partition_when_value_is_0(self):
        self.assertTrue(Solution().canPartitionKSubsets([0], 1))

    def test_can_partition_when_value_is_1(self):
        self.assertTrue(Solution().canPartitionKSubsets([1], 1))


class TestPartitionMultipleSubsets(TestCase):
    def test_can_partition_multiple_subsets(self):
        self.assertTrue(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))

    def test_can_partition_when_uneven_distribution(self):
        self.assertTrue(Solution().canPartitionKSubsets([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3))

    def test_cannot_partition_when_unique_k_numbers(self):
        self.assertFalse(Solution().canPartitionKSubsets([1, 2, 3], 3))
