from unittest import TestCase

from two_sum import Solution


class TestTwoSum(TestCase):
    def test_two_different(self):
        indices = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
        self.assertEqual(indices, [0, 1])

    def test_two_similar(self):
        indices = Solution().twoSum(nums=[1, 1, 2, 3], target=2)
        self.assertEqual(indices, [0, 1])
