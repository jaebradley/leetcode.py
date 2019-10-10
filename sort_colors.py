"""
https://leetcode.com/problems/sort-colors/

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.

First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's
and followed by 2's.

Could you come up with a one-pass algorithm using only constant space?

One-pass Approach:

Idea is to keep track of index for 0s, 1s, and 2s.
Increment the 1s index and swap with the last 0s or 2s index when the 1s index value is 0 or 2.

* Pointer for current index for 0s
* Pointer for current index for 1s
* Pointer for current index for 2s
* While pointer for current index for 1s is <= pointer for current index for 2s
  * Need to make it <= so that when swaps a 2 with a 0, the 0 can also get swapped
  * When the value for the current index for 1s is a 0, swap with the last current index for 0s pointer
    * Increment 0s index
    * Increment 1s index
    * Since initial 1s index is same as initial 0s index, if first value is a 2, that 2 will get swapped properly.
      That's why can increment both 0s index and 1s index
  * When the value for the current index for 1s is a 1, value is in the correct place (order-wise)
    so just increment 1s index
  * When the value for the current index for 1s is a 2, swap with the last current index for 2s pointer
    * Decrement 2s index
    * Don't increment 1s index (this is to ensure that if the current 2s value is a 0, it will be handled by
      the 0 case in the next iteration of this loop)
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index_after_red = 0
        white_index = 0
        index_before_blue = len(nums) - 1

        while white_index <= index_before_blue:
            if nums[white_index] == 0:
                self.swap(nums, index_after_red, white_index)
                index_after_red += 1
                white_index += 1
            elif nums[white_index] == 1:
                white_index += 1
            elif nums[white_index] == 2:
                self.swap(nums, index_before_blue, white_index)
                index_before_blue -= 1

    def swap(self, nums, first_index, second_index):
        temp_first_value = nums[first_index]
        nums[first_index] = nums[second_index]
        nums[second_index] = temp_first_value
