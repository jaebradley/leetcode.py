from unittest import TestCase

from palindrome_partitioning import Solution


class TestPalindromePartitioning(TestCase):
    def test_three_letter(self):
        partitions = Solution().partition("aab")
        self.assertEqual(2, len(partitions))
        self.assertTrue(["aa", "b"] in partitions)
        self.assertTrue(["a", "a", "b"] in partitions)
