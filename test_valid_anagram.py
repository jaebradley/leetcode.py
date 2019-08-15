from unittest import TestCase


from valid_anagram import Solution


class TestAnagram(TestCase):
    def test_true_when_single_letter_matches(self):
        self.assertTrue(Solution().isAnagram("s", "s"))

    def test_false_when_single_letter_does_not_match(self):
        self.assertFalse(Solution().isAnagram("s", "t"))

    def test_true_when_identical_words_with_only_one_letter_match(self):
        self.assertTrue(Solution().isAnagram("ss", "ss"))

    def test_false_when_identical_words_with_different_letters_match(self):
        self.assertFalse(Solution().isAnagram("ss", "tt"))

    def test_false_when_expected_output_shorter_than_expected_input(self):
        self.assertFalse(Solution().isAnagram("ab", "b"))

    def test_true_when_expected_output_is_reverse_input(self):
        self.assertTrue(Solution().isAnagram("ab", "ba"))
