from unittest import TestCase

from partition_equal_subset_sum import Solution


class TestCannotPartition(TestCase):
    def test_when_two_unequal_values(self):
        self.assertFalse(Solution().canPartition([1, 2]))

    def test_single_value(self):
        self.assertFalse(Solution().canPartition([1]))

    def test_unable_to_sum(self):
        self.assertFalse(Solution().canPartition([1, 2, 3, 5]))


class TestCanBePartitioned(TestCase):
    def test_can_be_partitioned_when_same_elements(self):
        self.assertTrue(Solution().canPartition([1, 1]))

    def test_can_be_partitioned_when_one_element_is_sum_of_remaining_elements(self):
        self.assertTrue(Solution().canPartition([1, 2, 3, 6]))

    def test_sum_of_different_elements(self):
        self.assertTrue(Solution().canPartition([10, 10, 10, 6, 6, 6, 4, 4, 4]))
