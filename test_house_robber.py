from unittest import TestCase

from house_robber import Solution


class TestHouseRobber(TestCase):
    def test_skip_first_house(self):
        self.assertEqual(Solution().rob([1, 10, 1, 1]), 11)

    def test_every_other_starting_with_first(self):
        self.assertEqual(Solution().rob([1, 2, 3, 2, 4]), 8)

    def test_large_test_case(self):
        self.assertEqual(Solution().rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]), 3365)
