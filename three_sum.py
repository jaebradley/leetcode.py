"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        Strategy is to use sort first and then use three pointers:
        1. One pointer is current value
        2. One pointer is "left" index that starts from index after current value
        3. One pointer is "right" index that starts from last index

        Calculate sum of all three pointers.
        If sum is greater than 0, need to make sum smaller, so decrease right index until next distinct integer
        If sum is less than 0, need to make bigger, so increase left index until next distinct integer
        If sum is 0, we found combination that works - when combination is found, need to increment left and right
          indices until next distinct integers for both.

        When left index surpasses right index, stop iterating and move on to next value.
        Can only calculate sums when current value is not positive. This is because three positive values can't sum to 0.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []

        nums.sort()

        for index, target in enumerate(nums[:-2]):
            if target <= 0 and (index == 0 or (index > 0 and nums[index] != nums[index - 1])):
                left_index = index + 1
                right_index = len(nums) - 1

                while left_index < right_index:
                    triplet_sum = target + nums[left_index] + nums[right_index]

                    if triplet_sum > 0:
                        right_value = nums[right_index]
                        while left_index < right_index and right_value == nums[right_index]:
                            right_index -= 1
                    elif triplet_sum < 0:
                        left_value = nums[left_index]
                        while left_index < right_index and left_value == nums[left_index]:
                            left_index += 1
                    else:
                        triplets.append([
                            target,
                            nums[left_index],
                            nums[right_index],
                        ])

                        right_value = nums[right_index]
                        while left_index < right_index and right_value == nums[right_index]:
                            right_index -= 1

                        left_value = nums[left_index]
                        while left_index < right_index and left_value == nums[left_index]:
                            left_index += 1

        return triplets
