from unittest import TestCase

from longest_repeating_character_replacement import Solution


class TestEmptyString(TestCase):
    def test_it_is_zero(self):
        self.assertEqual(0, Solution().characterReplacement("", 1))


class ZeroReplacementOperations(TestCase):
    def test_when_longest_substring_is_in_middle_of_string_it_returns_length_of_longest_continuous_substring(self):
        self.assertEqual(3, Solution().characterReplacement("ABBBA", 0))

    def test_when_longest_substring_is_at_start_of_string_it_returns_length_of_longest_continuous_substring(self):
        self.assertEqual(3, Solution().characterReplacement("AAABBC", 0))

    def test_when_longest_substring_is_at_end_of_string_it_returns_length_of_longest_continuous_substring(self):
        self.assertEqual(3, Solution().characterReplacement("CBBAAA", 0))


class SingleReplacementOperation(TestCase):
    def test_when_replacement_operation_occurs_in_middle_of_string(self):
        self.assertEqual(4, Solution().characterReplacement("ABBABA", 1))


class TestSingleAlternating(TestCase):
    def test_it_is_three(self):
        self.assertEqual(3, Solution().characterReplacement("ABA", 3))

    def test_it_is_6(self):
        self.assertEqual(6, Solution().characterReplacement("ABABAB", 3))


class TestAllSameCharacter(TestCase):
    def test_it_is_three(self):
        self.assertEqual(3, Solution().characterReplacement("AAA", 3))
