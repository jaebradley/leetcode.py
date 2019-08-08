from unittest import TestCase

from remove_invalid_parentheses import Solution


class TestWithoutRemoval(TestCase):
    def test_empty_string(self):
        self.assertEqual([""], Solution().removeInvalidParentheses(""))

    def test_string_without_parentheses(self):
        self.assertEqual(["jaebaebae"], Solution().removeInvalidParentheses(""))


class TestSingleRemoval(TestCase):
    def test_single_removal_with_two_valid_solutions(self):
        self.assertEqual(
            [
                "()()()",
                "(())()",
            ],
            Solution().removeInvalidParentheses("()())()")
        )

    def test_single_removal_with_two_valid_solutions_with_non_parentheses_character(self):
        self.assertEqual(
            [
                "(a)()()",
                "(a())()",
            ],
            Solution().removeInvalidParentheses("(a)())()")
        )
