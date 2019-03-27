"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        Strategy is to keep track of current sum and max sum so far.
        Initially assign current sum to first value in list.
        As iterate through values, if sum of value and next value is less than next value, should just start calculating using next value.
        (Imagine case of -10 then 10 then a whole bunch of positive numbers - the sum will be larger when using 10 vs. considering both -10 AND 10.)
        If the current sum is > max sum, then reassign as there is a new max sum.
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = current_sum
        for num in nums[1:]:
            potential_next_sum = current_sum + num
            if potential_next_sum < num:
                current_sum = num
            else:
                current_sum = potential_next_sum
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
