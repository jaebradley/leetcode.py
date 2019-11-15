from unittest import TestCase

from remove_invalid_parentheses import Solution


class TestWithoutRemoval(TestCase):
    def test_empty_string(self):
        self.assertEqual([""], Solution().removeInvalidParentheses(""))

    def test_string_without_parentheses(self):
        self.assertEqual([""], Solution().removeInvalidParentheses(""))


class TestSingleRemoval(TestCase):
    def test_single_removal_with_two_valid_solutions(self):
        valid_values = Solution().removeInvalidParentheses("()())()")
        self.assertIn("(())()", valid_values)
        self.assertIn("()()()", valid_values)

    def test_single_removal_with_two_valid_solutions_with_non_parentheses_character(self):
        valid_values = Solution().removeInvalidParentheses("(a)())()")
        self.assertIn("(a)()()", valid_values)
        self.assertIn("(a())()", valid_values)

