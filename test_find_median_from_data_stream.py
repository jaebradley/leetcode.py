from unittest import TestCase

from find_median_from_data_stream import MedianFinder


class TestMedianFinder(TestCase):
    def test_two(self):
        finder = MedianFinder()
        finder.addNum(1)
        finder.addNum(2)
        self.assertEqual(1.5, finder.findMedian())

    def test_one(self):
        finder = MedianFinder()
        finder.addNum(1)
        self.assertEqual(1, finder.findMedian())

    def test_three(self):
        finder = MedianFinder()
        finder.addNum(1)
        finder.addNum(2)
        finder.addNum(3)
        self.assertEqual(2, finder.findMedian())
