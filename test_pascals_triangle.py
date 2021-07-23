from unittest import TestCase
from pascals_triangle import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_generate(self):
        self.assertListEqual(
            [[1]],
            self.solution.generate(1)
        )

        self.assertListEqual(
            [[1], [1, 1]],
            self.solution.generate(2)
        )

        self.assertListEqual(
            [[1], [1, 1], [1, 2, 1]],
            self.solution.generate(3)
        )

        self.assertListEqual(
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]],
            self.solution.generate(4)
        )

        self.assertListEqual(
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
            self.solution.generate(5)
        )
