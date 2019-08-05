from unittest import TestCase

from number_of_longest_increasing_subsequence import Solution


class TestAllSameNumbers(TestCase):
    def test_longest_subsequence_is_length_of_input(self):
        self.assertEqual(5, Solution().findNumberOfLIS([2, 2, 2, 2]))


class TestSingleNumberDecreasingSequence(TestCase):
    def test_starts_with_decreasing_sequence(self):
        self.assertEqual(2, Solution().findNumberOfLIS([5, 4, 6, 7]))

    def test_middle_decreasing_sequence(self):
        self.assertEqual(2, Solution().findNumberOfLIS([3, 5, 4, 6]))

    def test_end_decreasing_sequence(self):
        self.assertEqual(2, Solution().findNumberOfLIS([3, 4, 6, 5]))
