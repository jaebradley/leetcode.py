from unittest import TestCase

from longest_palindromic_subsequence import Solution


class TestLongestPalindromicSubsequence(TestCase):
    def test_bbbab_should_be_bbbb(self):
        self.assertEqual(4, Solution().longestPalindromeSubseq("bbbab"))
