from unittest import TestCase

from wiggle_subsequence import Solution


class TestWiggleSubsequence(TestCase):
    def test_when_already_wiggle_subsequence(self):
        self.assertEqual(
            5,
            Solution().wiggleMaxLength([1, 3, 2, 4, 0])
        )

    def test_when_remove_some(self):
        self.assertEqual(
            7,
            Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
        )
