from unittest import TestCase

from longest_substring_without_repeating_characters import Solution


class TestSingleCharacter(TestCase):
    def test_length_is_1(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("a"))


class TestDoubleDuplicateCharacters(TestCase):
    def test_length_is_1(self):
        self.assertEqual(1, Solution().lengthOfLongestSubstring("aa"))


class TestSeparateDuplicateCharacters(TestCase):
    def test_length_is_2(self):
        self.assertEqual(2, Solution().lengthOfLongestSubstring("aba"))


class TestInterleavedCharacters(TestCase):
    def test_length_is_2(self):
        self.assertEqual(2, Solution().lengthOfLongestSubstring("abab"))


class TestEmptyString(TestCase):
    def test_length_is_0(self):
        self.assertEqual(0, Solution().lengthOfLongestSubstring(""))


class TestDoubleSeparatingTwoCharacters(TestCase):
    def test_length_is_2(self):
        self.assertEqual(2, Solution().lengthOfLongestSubstring("abba"))
