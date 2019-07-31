"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        There are two states needed to keep track of - the first is max profit when nothing has been bought, the second
        is max profit when one thing has been bought.

        The max profit when nothing has been bought is the max of current value or when one thing has been sold minus
        the day's price minus the transaction fee.

        The max profit when something has been bought is the max of current value or value when nothing has been bought
        minus day's price minus the transaction fee.

        Start with value of buying nothing as 0. Start with value of buying something as -Infinity.
        For each day, check to see if previous something bought + day's price is greater than last nothing bought.

        Initially, this means that max when nothing has been bought is 0 and when something has been bought is -first
        day's price - transaction fee.

        Will only trade if profit after last buy + day's price is greater than when nothing was bought in first place.

        O(n) runtime as go through prices one day at a time, once.

        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        max_nothing_bought = 0
        max_something_bought = -float("inf")

        for price in prices:
            old_nothing_bought = max_nothing_bought
            max_nothing_bought = max(old_nothing_bought, max_something_bought + price)
            max_something_bought = max(max_something_bought, old_nothing_bought - price - fee)

        return max(max_nothing_bought, max_something_bought)
