from unittest import TestCase

from word_break import Solution


class TestWordBreak(TestCase):
    def test_separation(self):
        self.assertTrue(Solution().wordBreak("leetcode", ["leet", "code"]))

    def test_reusing_dictionary_word(self):
        self.assertTrue(Solution().wordBreak("applepenapple", ["apple", "pen"]))

    def test_dictionary_words_that_share_root(self):
        self.assertTrue(Solution().wordBreak("applebloom", ["app", "apple", "lebloom"]))

    def test_use_second_matching_dictionary_word(self):
        self.assertTrue(Solution().wordBreak("applebloom", ["apple", "app", "lebloom"]))

    def test_not_enough_characters(self):
        self.assertFalse(Solution().wordBreak("aaaaaaa", ["aaaa","aa"]))
