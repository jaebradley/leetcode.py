from unittest import TestCase

from unique_paths_2 import Solution


class TestSingleObstacle(TestCase):
    def test_three_by_three_with_middle_obstacle(self):
        self.assertEqual(
            2,
            Solution().uniquePathsWithObstacles(
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]
                ]
            ))

    def test_two_by_two_with_right_obstacle(self):
        self.assertEqual(
            1,
            Solution().uniquePathsWithObstacles(
                [
                    [0, 1],
                    [0, 0],
                ]
            )
        )

    def test_two_by_two_with_down_obstacle(self):
        self.assertEqual(
            1,
            Solution().uniquePathsWithObstacles(
                [
                    [0, 0],
                    [1, 0],
                ]
            )
        )

    def test_two_by_two_with_starting_obstacle(self):
        self.assertEqual(
            0,
            Solution().uniquePathsWithObstacles(
                [
                    [1, 0],
                    [0, 0],
                ]
            )
        )

    def test_one_by_one_with_no_obstacle(self):
        self.assertEqual(
            1,
            Solution().uniquePathsWithObstacles(
                [
                    [0]
                ]
            )
        )

    def test_one_by_one_with_obstacle(self):
        self.assertEqual(
            0,
            Solution().uniquePathsWithObstacles(
                [
                    [1]
                ]
            )
        )

    def test_one_by_two_with_no_obstacle(self):
        self.assertEqual(
            1,
            Solution().uniquePathsWithObstacles(
                [
                    [0, 0]
                ]
            )
        )

    def test_one_by_two_with_an_end_obstacle(self):
        self.assertEqual(
            0,
            Solution().uniquePathsWithObstacles(
                [
                    [0, 1]
                ]
            )
        )

    def test_one_by_two_with_a_start_obstacle(self):
        self.assertEqual(
            0,
            Solution().uniquePathsWithObstacles(
                [
                    [1, 0]
                ]
            )
        )


class TestMultipleObstacles(TestCase):
    def test_two_by_two_with_left_and_down_obstacles(self):
        self.assertEqual(
            0,
            Solution().uniquePathsWithObstacles(
                [
                    [0, 1],
                    [1, 0],
                ]
            )
        )

    def test_three_by_three_with_left_and_down_obstaclse(self):
        self.assertEqual(
            0,
            Solution().uniquePathsWithObstacles(
                [
                    [0, 1, 0],
                    [1, 0, 0],
                    [0, 0, 0]
                ]
            ))
