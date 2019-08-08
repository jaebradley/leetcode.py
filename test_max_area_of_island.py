from unittest import TestCase

from max_area_of_island import Solution


class TestMaxArea(TestCase):
    def test_island(self):
        self.assertEqual(6, Solution().maxAreaOfIsland(
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
            ]
        ))

    def test_single_row_of_zeros(self):
        self.assertEqual(0, Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))

    def test_single_island_in_row(self):
        self.assertEqual(1, Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 1, 0, 0]]))

    def test_single_set_of_islands_in_row(self):
        self.assertEqual(3, Solution().maxAreaOfIsland([[0, 0, 1, 1, 1, 0, 0, 0]]))

    def test_diagonal(self):
        self.assertEqual(1, Solution().maxAreaOfIsland(
            [
                [0, 0, 1],
                [0, 1, 0],
            ]
        ))

    def test(self):
        self.assertEqual(4, Solution().maxAreaOfIsland(
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]
            ]
        ))
