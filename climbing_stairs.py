"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution(object):
    def __init__(self):
        self.stairs = [0, 1, 2]

    def climbStairs(self, n):
        """
        Strategy is to see that next stairs count are a combination of previous stairs count.
        The number of ways to climb the nth stairs is the number of ways to climb the n-1 stairs + n-2 stairs.
        From n-1 stairs there's only one way to get to the nth stair and from the n-2 stairs there's only one way to
        get to the nth stair.
        :type n: int
        :rtype: int
        """
        if n > 2:
            self.climbStairs(n - 1)
            self.stairs.insert(n, self.stairs[n - 1] + self.stairs[n - 2])

        return self.stairs[n]
