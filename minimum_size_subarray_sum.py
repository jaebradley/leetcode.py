"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
 which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        Initial minimum length is maximum infinity.
        Start index is 0 and end index is 0.
        Current sum is start index.
        Increment end index and add new values to current sum until above s.
        Once above s, increment start index, decreasing from current sum until below s.
        Take note of length (i.e. end index - start index) on each loop and update minimum length.
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        minimum_length = float("infinity")
        start_index = 0
        end_index = 0
        current_sum = 0

        while end_index < len(nums):
            current_sum += nums[end_index]
            end_index += 1

            while current_sum >= s:
                minimum_length = min(minimum_length, end_index - start_index)
                current_sum -= nums[start_index]
                start_index += 1

        return 0 if minimum_length == float("infinity") else minimum_length

