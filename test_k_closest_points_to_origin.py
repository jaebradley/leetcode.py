from unittest import TestCase

from k_closest_points_to_origin import Solution


class TestEmptyPoints(TestCase):
    def setUp(self) -> None:
        self.points = []

    def test_returns_empty_array_when_k_is_0(self):
        self.assertListEqual(Solution().kClosest(self.points, 0), [])

    def test_returns_empty_array_when_k_is_1(self):
        self.assertListEqual(Solution().kClosest(self.points, 1), [])


class TestSinglePoint(TestCase):
    def setUp(self) -> None:
        self.points = [[1, 1]]

    def test_returns_empty_array_when_k_is_0(self):
        self.assertListEqual(Solution().kClosest(self.points, 0), [])

    def test_returns_point_when_k_is_1(self):
        self.assertListEqual(Solution().kClosest(self.points, 1), [[1, 1]])


class TestTwoPoints(TestCase):
    def setUp(self) -> None:
        self.points = [[1, 1], [2, 1]]

    def test_returns_empty_array_when_k_is_0(self):
        self.assertListEqual(Solution().kClosest(self.points, 0), [])

    def test_returns_closest_point_when_k_is_1(self):
        self.assertListEqual(Solution().kClosest(self.points, 1), [[1, 1]])

    def test_returns_points_when_k_is_2(self):
        points = Solution().kClosest(self.points, 2)
        self.assertTrue(len(points), 2)
        self.assertTrue([1, 1] in points)
        self.assertTrue([2, 1] in points)


class TestThreePoints(TestCase):
    def setUp(self) -> None:
        self.points = [
            [1, 1],
            [1, 2],
            [1, 3]
        ]

    def test_returns_empty_array_when_k_is_0(self):
        self.assertListEqual(Solution().kClosest(self.points, 0), [])

    def test_returns_closest_point_when_k_is_1(self):
        self.assertListEqual(Solution().kClosest(self.points, 1), [[1, 1]])

    def test_returns_two_closest_points_when_k_is_2(self):
        points = Solution().kClosest(self.points, 2)
        self.assertTrue(len(points), 2)
        self.assertTrue([1, 1] in points)
        self.assertTrue([1, 2] in points)

    def test_returns_three_closest_points_when_k_is_3(self):
        points = Solution().kClosest(self.points, 3)
        self.assertTrue(len(points), 3)
        self.assertTrue([1, 1] in points)
        self.assertTrue([1, 2] in points)
        self.assertTrue([1, 3] in points)
