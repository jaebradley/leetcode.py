from unittest import TestCase

from shortest_unsorted_continuous_subarray import Solution


class TestShortestUnsortedContinuousSubarray(TestCase):
    def test_all_increasing(self):
        self.assertEqual(0, Solution().findUnsortedSubarray([1, 2, 3, 4, 5]))

    def test_all_equal(self):
        self.assertEqual(0, Solution().findUnsortedSubarray([1, 1, 1, 1]))

    def test_empty(self):
        self.assertEqual(0, Solution().findUnsortedSubarray([]))

    def test_single(self):
        self.assertEqual(0, Solution().findUnsortedSubarray([1]))

    def test_five(self):
        self.assertEqual(5, Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

    def test_two(self):
        self.assertEqual(2, Solution().findUnsortedSubarray([1, 3, 2, 4, 5]))

    def test_four(self):
        self.assertEqual(4, Solution().findUnsortedSubarray([1, 3, 2, 2, 2]))
