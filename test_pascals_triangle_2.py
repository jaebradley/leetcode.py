from unittest import TestCase

from pascals_triangle_2 import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_get_row(self):
        self.assertListEqual(
            [1],
            self.solution.getRow(0)
        )

        self.assertListEqual(
            [1, 1],
            self.solution.getRow(1)
        )

        self.assertListEqual(
            [1, 2, 1],
            self.solution.getRow(2)
        )

        self.assertListEqual(
            [1, 3, 3, 1],
            self.solution.getRow(3)
        )

        self.assertListEqual(
            [1, 4, 6, 4, 1],
            self.solution.getRow(4)
        )
