from unittest import TestCase

from minimum_ascii_delete_sum_for_two_strings import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_sea_eat(self):
        self.assertEqual(
            231,
            self.solution.minimumDeleteSum("sea", "eat")
        )

    def test_delete_leet(self):
        self.assertEqual(
            403,
            self.solution.minimumDeleteSum("delete", "leet")
        )
