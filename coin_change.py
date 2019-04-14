"""
https://leetcode.com/problems/coin-change/
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        Strategy is to use dynamic programming and keep prior calculations in dictionary.
        The idea is that the minimum coins for a given sum is the minimum coins for the given sum minus one of the coin
        values, plus 1.
        Starting from 0 and incrementing by 1, try and calculate the minimum coins, using the above philosophy.
        If a value is uncalculable, use default value (negative infinity) in this case.
        If a value is calculable, take the min after applying each coin value subtraction.
        At the end, if the value of the given amount is the default value, it's uncalculable and return -1.
        Else it is calculable and return the given amount.
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1

        coin_sums_count = {0: 0}
        coin_sum = 0
        default_value = float('inf')

        while coin_sum < amount:
            coin_sum += 1
            min_count = default_value

            for coin in coins:
                difference = coin_sum - coin
                if difference >= 0:
                    min_count = min(coin_sums_count[difference] + 1, min_count)

            coin_sums_count[coin_sum] = min_count

        if coin_sums_count[amount] == default_value:
            return -1

        return coin_sums_count[amount]

