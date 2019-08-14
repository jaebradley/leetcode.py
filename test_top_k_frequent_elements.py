from unittest import TestCase

from top_k_frequent_elements import Solution


class TestTopKFrequentElements(TestCase):
    def test_top_1(self):
        self.assertEqual(
            [1],
            Solution().topKFrequent([1], 1)
        )

    def test_top_2(self):
        self.assertEqual(
            [1, 2],
            Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
        )

    def test_top_2_input_numerically_decreasing(self):
        self.assertEqual(
            [1, 2],
            Solution().topKFrequent([3, 2, 2, 1, 1, 1], 2)
        )


class TestTopKFrequentElementsBucketSort(TestCase):
    def test_top_1(self):
        self.assertEqual(
            [1],
            Solution().bucketSort([1], 1)
        )

    def test_top_2(self):
        self.assertEqual(
            [1, 2],
            Solution().bucketSort([1, 1, 1, 2, 2, 3], 2)
        )

    def test_top_2_input_numerically_decreasing(self):
        self.assertEqual(
            [1, 2],
            Solution().bucketSort([3, 2, 2, 1, 1, 1], 2)
        )

