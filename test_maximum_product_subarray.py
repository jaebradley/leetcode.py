from unittest import TestCase

from maximum_product_subarray import Solution


class TestMaximumProductSubarray(TestCase):
    def test_with_positive_numbers(self):
        self.assertEqual(Solution().maxProduct([1, 2, 3, 4]), 24)

    def test_with_positive_numbers_with_zero_at_beginning(self):
        self.assertEqual(Solution().maxProduct([0, 4, 5]), 20)

    def test_with_positive_numbers_with_zero_in_the_middle(self):
        self.assertEqual(Solution().maxProduct([4, 0, 5]), 5)

    def test_with_positive_numbers_with_zero_at_end(self):
        self.assertEqual(Solution().maxProduct([4, 5, 0]), 20)

    def test_with_even_number_of_negative_numbers(self):
        self.assertEqual(Solution().maxProduct([-1, -2, -3, -4]), 24)

    def test_with_negative_numbers_with_zero_at_beginning(self):
        self.assertEqual(Solution().maxProduct([0, -4, -5]), 20)

    def test_with_negative_numbers_with_zero_in_the_middle(self):
        self.assertEqual(Solution().maxProduct([-4, 0, -5]), 0)

    def test_with_negative_numbers_with_zero_at_end(self):
        self.assertEqual(Solution().maxProduct([-4, -5, 0]), 20)

    def test_with_odd_number_of_negative_numbers_with_zero_at_beginning(self):
        self.assertEqual(Solution().maxProduct([0, 4, -5]), 4)

    def test_with_odd_numbers_of_negative_numbers_with_zero_in_the_middle(self):
        self.assertEqual(Solution().maxProduct([4, 0, -5]), 4)

    def test_with_odd_numbers_of_negative_numbers_with_zero_at_end(self):
        self.assertEqual(Solution().maxProduct([4, -5, 0]), 4)
