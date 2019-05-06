from unittest import TestCase


from non_overlapping_intervals import Solution


class TestSolution(TestCase):
    def test_identical_intervals(self):
        intervals = [
            [1, 2],
            [1, 2],
            [1, 2],
        ]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 2)

    def test_three_intervals_where_one_is_overlapping(self):
        intervals = [
            [1, 3],
            [2, 4],
            [3, 5],
        ]

        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 1)

    def test_three_intervals_where_all_are_bordering_each_other(self):
        intervals = [
            [1, 2],
            [2, 3],
            [3, 4],
        ]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_three_non_overlapping_or_touching_intervals(self):
        intervals = [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)
