"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_numbers = set(nums)
        max_length = 0

        for num in distinct_numbers:
            if num - 1 not in distinct_numbers:
                count = 0
                next_num = num

                while next_num in distinct_numbers:
                    count += 1
                    next_num += 1

                max_length = max(max_length, count)

        return max_length
