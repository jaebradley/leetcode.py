from unittest import TestCase

from longest_consecutive_sequence import Solution


class TestLongestConsecutiveSequence(TestCase):
    def test_out_of_order(self):
        self.assertEqual(4, Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

    def test_in_order(self):
        self.assertEqual(4, Solution().longestConsecutive([1, 2, 3, 4]))

    def test_in_reverse_order(self):
        self.assertEqual(4, Solution().longestConsecutive([4, 3, 2, 1]))

    def test_all_same_numbers(self):
        self.assertEqual(1, Solution().longestConsecutive([1, 1, 1, 1, 1]))
