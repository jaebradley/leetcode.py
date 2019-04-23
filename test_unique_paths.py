from unittest import TestCase


from unique_paths import Solution


class TestUniquePaths(TestCase):
    def test_one_by_one(self):
        self.assertEqual(Solution().uniquePaths(1, 1), 1)

    def test_two_by_one(self):
        self.assertEqual(Solution().uniquePaths(2, 1), 1)

    def test_one_by_two(self):
        self.assertEqual(Solution().uniquePaths(1, 2), 1)

    def test_two_by_two(self):
        self.assertEqual(Solution().uniquePaths(2, 2), 2)

    def test_three_by_two(self):
        self.assertEqual(Solution().uniquePaths(3, 2), 3)

    def test_seven_by_three(self):
        self.assertEqual(Solution().uniquePaths(7, 3), 28)
