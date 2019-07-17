from unittest import TestCase

from word_search import Solution


class TestWordSearch(TestCase):
    def setUp(self):
        self.board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]

    def test_word_exists(self):
        self.assertTrue(Solution().exist(self.board, "ABCCED"))

    def test_word_does_not_exist(self):
        self.assertFalse(Solution().exist(self.board, "JAEBAEBAE"))

    def test_word_does_exist(self):
        self.assertTrue(Solution().exist(self.board, "CES"))

    def test_word_does_not_exist_2(self):
        self.assertFalse(Solution().exist(self.board, "SAF"))
