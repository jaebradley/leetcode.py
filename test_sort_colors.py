from unittest import TestCase

from sort_colors import Solution


class TestSortColors(TestCase):
    def test_sort_when_in_order(self):
        values = [0, 1, 2]
        Solution().sortColors(values)
        self.assertEqual(values, [0, 1, 2])

    def test_sort_when_in_reverse_order(self):
        values = [2, 1, 0]
        Solution().sortColors(values)
        self.assertEqual(values, [0, 1, 2])
