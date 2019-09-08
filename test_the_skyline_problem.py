from unittest import TestCase

from the_skyline_problem import Solution


class TestSkylineProblem(TestCase):
    def test_the_skyline_problem(self):
        self.assertEqual(
            [
                [2, 10],
                [3, 15],
                [7, 12],
                [12, 0],
                [15, 10],
                [20, 8],
                [24, 0]
            ],
            Solution().getSkyline([
                [2, 9, 10],
                [3, 7, 15],
                [5, 12, 12],
                [15, 20, 10],
                [19, 24, 8],
            ])
        )