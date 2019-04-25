from unittest import TestCase

from house_robber_two import Solution


class TestHouseRobberTwo(TestCase):
    def test_three_houses_selecting_second(self):
        self.assertEqual(Solution().rob([2, 3, 2]), 3)

    def test_four_houses_selecting_first(self):
        self.assertEqual(Solution().rob([1, 2, 3, 1]), 4)

    def test_four_houses_selecting_second(self):
        self.assertEqual(Solution().rob([10, 1, 2, 3]), 12)

    def test_two_houses_selecting_first(self):
        self.assertEqual(Solution().rob([1, 2]), 2)

    def test_two_houses_selecting_second(self):
        self.assertEqual(Solution().rob([2, 1]), 2)

    def test_one_house(self):
        self.assertEqual(Solution().rob([1]), 1)

    def test_empty(self):
        self.assertEqual(Solution().rob([]), 0)
