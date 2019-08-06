"""
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        Reverse the first n - k elements (where k has been modulo-ed properly.
        Reverse rest of the elements.
        Reverse entire array.

        Values that don't need to wrap can just be moved to i + k.
        Values that need to wrap can be moved to i + k - n.

        Runtime is O(n), O(1) space
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums is None or k <= 0:
            return

        step_rotations = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1 - step_rotations)
        self.reverse(nums, len(nums) - step_rotations, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start_index, end_index):
        while start_index < end_index:
            start_value = nums[start_index]
            nums[start_index] = nums[end_index]
            nums[end_index] = start_value
            start_index += 1
            end_index -= 1
