from unittest import TestCase


from generate_parentheses import Solution


class TestGenerateParentheses(TestCase):
    def test_2(self):
        parentheses = Solution().generateParenthesis(2)
        self.assertEqual(2, len(parentheses))
        self.assertTrue("(())" in parentheses)
        self.assertTrue("()()" in parentheses)

    def test_3(self):
        parentheses = Solution().generateParenthesis(3)
        self.assertEqual(5, len(parentheses))
        self.assertTrue("((()))" in parentheses)
        self.assertTrue("(()())" in parentheses)
        self.assertTrue("(())()" in parentheses)
        self.assertTrue("()(())" in parentheses)
        self.assertTrue("()()()" in parentheses)
