"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""


class Solution(object):
    def rob(self, nums):
        """
        There are two cases:
        1. Rob first house and calculate optimal robbing for all houses except the last
        2. Rob second house and calculate optimal robbing for all houses including the last

        For each scenario, keep track of three variables
        1. Max value from three houses ago
        2. Max value from two houses ago
        3. Max value from previous house

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(
            self.calculate_maximum_robbery(nums[:-1]),
            self.calculate_maximum_robbery(nums[1:]),
        )

    def calculate_maximum_robbery(self, houses):
        maximum_value_three_houses_prior = 0
        maximum_value_two_houses_prior = 0
        maximum_value_one_house_prior = 0

        for house in houses:
            next_maximum_value_one_house_prior = max(
                maximum_value_three_houses_prior + house,
                maximum_value_two_houses_prior + house,
            )
            maximum_value_three_houses_prior = maximum_value_two_houses_prior
            maximum_value_two_houses_prior = maximum_value_one_house_prior
            maximum_value_one_house_prior = next_maximum_value_one_house_prior

        return max(
            maximum_value_one_house_prior,
            maximum_value_two_houses_prior
        )
