from unittest import TestCase
from maximum_length_of_pair_chain import Solution


class TestSolution(TestCase):
    def test_overlapping_intervals(self):
        self.assertEqual(
            2,
            Solution().findLongestChain([
                [1, 2],
                [2, 3],
                [3, 4]
            ])
        )

    def test_non_overlapping_intervals(self):
        self.assertEqual(
            3,
            Solution().findLongestChain([
                [1, 2],
                [7, 8],
                [4, 5]
            ])
        )
