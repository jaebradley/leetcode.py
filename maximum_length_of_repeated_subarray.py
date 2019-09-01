"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""


class Solution(object):
    def findLength(self, A, B):
        """
        Build a 2D matrix where max_lengths[i][j] represents the maximum length of subarray for value A[i] and B[j].
        If A[i] and B[j] are the same then the max length is 1 + max_length[i - 1][j - 1].
        If A[i] and B[j] aren't the same then don't consider them as they can't be part of same subarray.
        Runtime is O(m * n) where m and n are the sizes of A and B, respectively.
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if A is None or B is None:
            return 0

        max_length = 0
        max_lengths = []
        for i in range(len(A)):
            max_lengths.append([])
            for j in range(len(B)):
                max_lengths[i].append(0)

        for i in range(0, len(A)):
            for j in range(0, len(B)):
                a_char = A[i]
                b_char = B[j]

                if a_char == b_char:
                    if i == 0 or j == 0:
                        max_lengths[i][j] = 1
                    else:
                        max_lengths[i][j] = 1 + max_lengths[i - 1][j - 1]
                    max_length = max(max_length, max_lengths[i][j])

        return max_length
