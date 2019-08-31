from unittest import TestCase

from longest_increasing_subsequence import Solution


class TestLIS(TestCase):
    def test_longest_middle_skipping_single_value_subsequence(self):
        self.assertEqual(4, Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
