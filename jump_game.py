"""
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def canJump(self, nums):
        """
        Strategy is to keep track of the maximum index that can be reached.

        There 1 way to change the maximum index.

        Using the number at a given index and then adding the current index to that number - this should
        give the maximum index reachable from that index. If this number is greater than the current max
        index, then use it.

        If the current index is greater than the max index, return False. This means an index was reached that
        a value at an index slot + the index value at that slot did not equal or surpass that index.

        :type nums: List[int]
        :rtype: bool
        """
        maximum_index = 0
        for index, num in enumerate(nums):
            if index > maximum_index:
                return False

            maximum_index = max(num + index, maximum_index)

        return True
