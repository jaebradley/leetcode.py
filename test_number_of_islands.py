from unittest import TestCase

from number_of_islands import Solution


class TestEmptyCases(TestCase):
    def test_zero_for_2_by_2(self):
        self.assertEqual(
            Solution().numIslands(
                [
                    ["0", "0"],
                    ["0", "0"],
                ]
            ),
            0
        )


class TestFilledTwoByTwo(TestCase):
    def test_is_one(self):
        self.assertEqual(
            Solution().numIslands(
                [
                    ["1", "1"],
                    ["1", "1"],
                ]
            ),
            1,
        )


class TestTwoIslandsInTwoByTwo(TestCase):
    def test_is_two(self):
        self.assertEqual(
            Solution().numIslands(
                [
                    ["1", "0"],
                    ["0", "1"],
                ]
            ),
            2,
        )


class TestAllButOneFilledTwoByTwo(TestCase):
    def test_is_one(self):
        self.assertEqual(
            Solution().numIslands(
                [
                    ["1", "0"],
                    ["1", "1"],
                ]
            ),
            1,
        )


