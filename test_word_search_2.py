from unittest import TestCase


from word_search_2 import Solution


class TestFindWords(TestCase):
    def test_finds_subset_of_words(self):
        found_words = Solution().findWords(
            [
                ['o', 'a', 'a', 'n'],
                ['e', 't', 'a', 'e'],
                ['i', 'h', 'k', 'r'],
                ['i', 'f', 'l', 'v']
            ],
            ["oath", "pea", "eat", "rain"]
        )
        self.assertEqual(2, len(found_words))
        self.assertTrue("oath" in found_words)
        self.assertTrue("eat" in found_words)

    def test_single_word(self):
        self.assertEqual(
            ["a"],
            Solution().findWords(
                [["a"]],
                ["a"]
            )
        )
