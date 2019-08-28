from unittest import TestCase


from insert_interval import Solution


class TestInsertInterval(TestCase):
    def test_merging_single_interval(self):
        self.assertEqual(
            [[1, 5], [6, 9]],
            Solution().insert([[1, 3], [6, 9]], [2, 5])
        )

    def test_merging_interval_over_many_intervals(self):
        self.assertEqual(
            [[1, 2], [3, 10], [12, 16]],
            Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
        )
