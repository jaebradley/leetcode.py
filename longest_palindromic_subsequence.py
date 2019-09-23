"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

Approach:

dp[i][j] represents the longest palindromic subsequence for substring from index i to index j.
dp[i][j] = dp[i + 1][j - 1] + 2 if character at i equals character at j.
Adding 2 because need to account for adding character at i and character at j.
If character at i does not equal character at j, then dp[i][j] is max of dp[i + 1][j] or dp[i][j - 1].
So max of substring starting from incremental start or substring ending one character before.
dp[0]0] = 1
Iterate backwards to build palindrome subsequence such that being at 0 will have longest palindrome subsequence to end.
"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = []
        for i in range(len(s)):
            results = []
            for j in range(len(s)):
                if i == j:
                    results.append(1)
                else:
                    results.append(0)
            dp.append(results)

        for i in range(len(s), -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]
