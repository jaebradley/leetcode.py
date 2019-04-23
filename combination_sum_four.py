"""
https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add
up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        Strategy is to say iterate from 0 to the target value.
        For each iteration, iterate through the numbers given.
        For each number iteration, subtract the number from the current loop value.
        For this difference, if it's greater than or equal to 0, check the number of ways the previous sum was counted.
        Add this to the number of ways the existing value could be counted.
        The idea is basically to use history of tracking previous counts to calculate next counts.
        No need to worry about double counting since no duplicates are given.
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sums = {0: 1}

        for value in range(target + 1):
            for num in nums:
                previous_number = value - num
                if previous_number >= 0:
                    sums[value] = sums.get(value, 0) + sums.get(previous_number, 0)

        return sums.get(target, 0)
