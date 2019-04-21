"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution(object):
    def rob(self, nums):
        """
        The idea is that in order to figure out the max sum for a given number, you need either the max sum from two
        houses before or from three houses before (since the max sum from one house before is not allowed).

        Given these numbers, the max sum for the current number would be the max from two houses before +
        the current value or the max from three houses before + current value.

        Each iteration of the loop through the house values would "push" the previous values down, so the new max sum
        from three houses before was the previous max sum from two houses before, etc.

        The initial implementation I had was even simpler and was built on the premise that the sum at number X is the
        max of number X + rob called recursively for the values after the next value OR rob called recursively using the
        values starting from the next value.

        However, this approach timed out.
        
        :type nums: List[int]
        :rtype: int
        """
        three_houses_before_sum = 0
        two_houses_before_sum = 0
        one_house_before_sum = 0

        for num in nums:
            max_so_far = max(
                three_houses_before_sum + num,
                two_houses_before_sum + num,
            )
            three_houses_before_sum = two_houses_before_sum
            two_houses_before_sum = one_house_before_sum
            one_house_before_sum = max_so_far

        return max(
            one_house_before_sum,
            two_houses_before_sum
        )
