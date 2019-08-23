from unittest import TestCase


from basic_calculator import Solution


class TestBasicCalculator(TestCase):
    def test_calculate_simple_addition_between_two_positive_integers(self):
        self.assertEqual(2, Solution().calculate("1 + 1"))

    def test_calculate_simple_subtraction_between_two_positive_integers(self):
        self.assertEqual(5, Solution().calculate("10 - 5"))

    def test_calculate_simple_addition_between_positive_integer_and_zero(self):
        self.assertEqual(1, Solution().calculate("1 + 0"))

    def test_multiple_parentheses(self):
        self.assertEqual(23, Solution().calculate("(1 + (4 + 5 + 2) - 3) + (6 + 8)"))

    def test_adding_single_nested_parentheses(self):
        self.assertEqual(9, Solution().calculate("1 + (4 + 5 + 2) - 3"))

    def test_subtracting_single_nested_parentheses(self):
        self.assertEqual(-13, Solution().calculate("1 - (4 + 5 + 2) - 3"))

    def test_subtracting_single_nested_parentheses_that_also_has_subtraction(self):
        self.assertEqual(-9, Solution().calculate("1 - (4 + 5 - 2) - 3"))

    def test_number(self):
        self.assertEqual(2147483647, Solution().calculate("2147483647"))

    def test_number_with_parentheses(self):
        self.assertEqual(2147483647, Solution().calculate("(2147483647)"))
