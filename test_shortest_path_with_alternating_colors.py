from unittest import TestCase
from shortest_path_with_alternating_colors import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_shortest_alternating_paths(self):
        self.assertListEqual(
            [0, 1, -1],
            self.solution.shortestAlternatingPaths(3, [[0, 1], [1, 2]], [])
        )

    def test_shortest_alternating_paths_single_red_and_blue(self):
        self.assertListEqual(
            [0, 1, 2],
            self.solution.shortestAlternatingPaths(3, [[0, 1]], [[1, 2]])
        )

    def test_no_other_entities(self):
        self.assertListEqual(
            [0, -1, -1],
            self.solution.shortestAlternatingPaths(3, [[1, 0]], [[2, 1]])
        )

    def test_5(self):
        self.assertListEqual(
            [0, 1, 2, 3, 7],
            self.solution.shortestAlternatingPaths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]])
        )
