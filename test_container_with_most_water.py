from unittest import TestCase

from container_with_most_water import Solution


class TestContainerWithMostWater(TestCase):
    def test_ends_have_maximum_area(self):
        self.assertEqual(Solution().maxArea([10, 1, 1, 1, 1, 10]), 50)

    def test_middle_has_maximum_area(self):
        self.assertEqual(Solution().maxArea([1, 1, 10, 10, 1, 1]), 10)

    def test_start_and_middle_have_maximum_area(self):
        self.assertEqual(Solution().maxArea([10, 1, 1, 1, 10, 1, 1, 1]), 40)

    def test_end_and_middle_have_maximum_area(self):
        self.assertEqual(Solution().maxArea([1, 1, 1, 1, 10, 1, 1, 10]), 30)

    def test_higher_middle_but_does_not_have_maximum_area(self):
        self.assertEqual(Solution().maxArea([1, 1, 1, 2, 1, 1, 1]), 6)

    def test_two_higher_middle_but_does_not_have_maximum_area(self):
        self.assertEqual(Solution().maxArea([1, 1, 3, 2, 1, 1, 1]), 6)
