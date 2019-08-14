"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parentheses = set()

        self.build_parentheses(n, n, "", parentheses)

        return list(parentheses)

    def build_parentheses(self, left, right, text, parentheses):
        if left > 0:
            self.build_parentheses(left - 1, right, text + "(", parentheses)

        if right > left:
            self.build_parentheses(left, right - 1, text + ")", parentheses)

        if left == 0 and right == 0:
            parentheses.add(text)
