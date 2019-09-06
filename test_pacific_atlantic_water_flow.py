from unittest import TestCase

from pacific_atlantic_water_flow import Solution


class TestPacificAtlanticWaterFlow(TestCase):
    def test_3x3_with_single_peak(self):
        matrix = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        positions = Solution().pacificAtlantic(matrix)
        self.assertEqual(7, len(positions))
        self.assertTrue((0, 4) in positions)
        self.assertTrue((1, 3) in positions)
        self.assertTrue((1, 4) in positions)
        self.assertTrue((2, 2) in positions)
        self.assertTrue((3, 0) in positions)
        self.assertTrue((3, 1) in positions)
        self.assertTrue((4, 0) in positions)

    def test_3x3(self):
        matrix = [
            [3, 3, 3],
            [3, 1, 3],
            [0, 2, 4],
        ]
        positions = Solution().pacificAtlantic(matrix)
        self.assertEqual(8, len(positions))
        self.assertTrue((0, 0) in positions)
        self.assertTrue((0, 1) in positions)
        self.assertTrue((0, 2) in positions)
        self.assertTrue((1, 0) in positions)
        self.assertTrue((1, 2) in positions)
        self.assertTrue((2, 0) in positions)
        self.assertTrue((2, 1) in positions)
        self.assertTrue((2, 2) in positions)
