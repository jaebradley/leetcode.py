"""
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Strategy:

1. Initialize wait values array of zeroes that is equivalent in length to input array
1. Loop through input values and keep track of index and current value
1. On each loop, while stack is not empty, and the current value is greater than the value at the index of the top value of the stack, pop the stack value, which should represent a previous value's index
1. With the popped stack value, update the value in the wait values array at the index of the popped stack value - the value should be the current index minus the popped stack value. This value represents the index of a previously smaller value. In this way, the things remaining in the stack are indices that haven't reached a local maximum yet
1. Add current index to stack
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        wait_values = [0] * len(T)
        stack = []
        for i, current_value in enumerate(T):
            while stack and current_value > T[stack[-1]]:
                previous_smaller_value_index = stack.pop()
                wait_values[previous_smaller_value_index] = i - previous_smaller_value_index
            stack.append(i)

        return wait_values

