from unittest import TestCase

from product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(TestCase):
    def test_values(self):
        self.assertEqual(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_values_2(self):
        self.assertEqual(Solution().productExceptSelf([2, 3, 4, 5]), [60, 40, 30, 24])
