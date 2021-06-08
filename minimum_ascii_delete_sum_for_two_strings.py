"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.



Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.


Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.

Solution:

1. dp[x][y] stores the minimum ASCII delete sum for s1[:x] and s2[:y]
2. When x is 0, the minimum is the ASCII sum of s2[:j]. When y is 0, the minimum is the ASCII sum of s1[:x]
3. When s1 and s2 end in the same character, the minimum ASCII sum solution includes deleting that character
4. If they do not end in the same character, the minimum ASCII sum solution is either deleting the last character of s1
   or deleting the last character of s2, and adding that ASCII value to the previous cell value in the row / column
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = []

        for index in range(len(s1) + 1):
            dp.append([0] * (len(s2) + 1))

        for s1_index in range(1, len(s1) + 1):
            dp[s1_index][0] = dp[s1_index - 1][0] + ord(s1[s1_index - 1])

        for s2_index in range(1, len(s2) + 1):
            dp[0][s2_index] = dp[0][s2_index - 1] + ord(s2[s2_index - 1])

        for s1_index in range(1, len(s1) + 1):
            for s2_index in range(1, len(s2) + 1):
                if s1[s1_index - 1] == s2[s2_index - 1]:
                    dp[s1_index][s2_index] = dp[s1_index - 1][s2_index - 1]
                else:
                    dp[s1_index][s2_index] = min(dp[s1_index][s2_index - 1] + ord(s2[s2_index - 1]),
                                                 dp[s1_index - 1][s2_index] + ord(s1[s1_index - 1]))
        return dp[-1][-1]
