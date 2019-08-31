"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution(object):
    def lengthOfLISDP(self, nums):
        """
        This O(n^2) approach uses DP.
        Each index contains the longest increasing subsequence at that index.

        When evaluating each index, iterate through previous values.

        If a previous number is less than current number, increment the LIS value at the current index, if LIS value
        is greater than existing LIS value.

        At the end of iterating through each current index value, if the LIS value at the current index is greater than
        the max LIS, use it.

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        values = [1] * len(nums)
        max_value = 1

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    values[i] = max(values[i], values[j] + 1)

            max_value = max(max_value, values[i])

        return max_value

    def lengthOfLIS(self, nums):
        """
        Keep track of the smallest value in an array, where the index of the array corresponds to the size of the
        subsequence.

        So index 0 of the array represents the smallest value of all subsequences with a size of 1.
        Index 1 of the array would correspond to the smallest value of all subsequences with a size of 2.

        As one iterates over the numbers in the inputted array, if the number is greater than any of the smallest
        values in any of the subsequences, then add it to the array for the next greatest subsequence size.

        This basically means that an increasing subsequence exists with the updated size since a smaller increasing
        subsequence existed with a lesser value, and we're iterating through the numbers.

        To find if any of the smallest subsequence values match, binary search through smallest values in subsequences
        array.

        Since smallest sequences value array could be N long in worst case, and since need to search over the array N
        times, the total runtime is O(N * log N).

        :type nums: List[int]
        :rtype: int
        """
        length_tail_min_values = [0] * len(nums)
        size = 0

        for num in nums:
            start = 0
            end = size

            while start != end:
                middle = int((start + end) / 2)
                if length_tail_min_values[middle] < num:
                    start = middle + 1
                else:
                    end = middle

            length_tail_min_values[start] = num
            size = max(start + 1, size)

        return size


