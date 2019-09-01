from unittest import TestCase

from maximum_length_of_repeated_subarray import Solution


class TestMaximumLengthOfRepeatedSubarray(TestCase):
    def test_different_start(self):
        self.assertEqual(3, Solution().findLength([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))