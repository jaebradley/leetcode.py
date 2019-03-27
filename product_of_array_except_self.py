"""
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of
space complexity analysis.)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        The product at a single index (excluding the value at that index) is the product of all values to the left and
        the product of all values to the right.

        So can create a product of all values multiplied against each other from left to right.
        And then same array from right to left.

        And then multiplying values together should generate products that exclude the value at the index.
        :type nums: List[int]
        :rtype: List[int]
        """
        left_products = [1]
        for index, num in enumerate(nums):
            left_products.append(left_products[index] * num)

        right_products = [1]
        for index, num in enumerate(reversed(nums)):
            right_products.append(right_products[index] * num)

        products_except_self = []
        for index, num in enumerate(nums):
            products_except_self.append(left_products[index] * right_products[len(nums) - index - 1])

        return products_except_self
