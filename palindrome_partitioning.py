"""
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        Start from beginning of string.
        Partition additional character at a time.
        If partition is palindrome, call function recursively for remaining substring.
        Build remaining substring such that if it's a palindrome, continue searching.
        O(n*(2^n))
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, path, results):
        if not s:
            results.append(path)
            return

        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], results)

    def is_palindrome(self, s):
        return s == s[::-1]
