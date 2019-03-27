"""
https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        Strategy is to start with first number and keep track of local continuous subarray.
        Also keep track of min and max in local continuous subarray.
        When a negative number is seen in subarray, flip local min and max (since it's negative).
        Set the subarray max to the max of current number or product of the local max and current number.
        Set the subarray min to the min of current number or product of the local min and current number.
        If the local max is greater than the global max, update global max.
        :type nums: List[int]
        :rtype: int
        """
        current_num = nums[0]
        max_product = current_num
        local_max = current_num
        local_min = current_num
        for num in nums[1:]:
            if num < 0:
                temp_local_max = local_max
                local_max = local_min
                local_min = temp_local_max
            local_max = max(num, local_max * num)
            local_min = min(num, local_min * num)
            max_product = max(max_product, local_max)
        return max_product
