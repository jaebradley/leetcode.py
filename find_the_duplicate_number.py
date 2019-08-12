"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least
one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        Similar concept to finding cycle in linked list.

        Use fast and slow pointer.

        When they meet, fast pointer will have traveled 2x and the slow pointer will have traveled x.
        Since they meet in the cycle, the difference, x, is a multiple of the length of the cycle.

        If assume length from start of list to start of cycle is y, then slow pointer has traveled in cycle for x - y
        steps.

        To get slow pointer back to start of cycle, need to travel y steps.
        Can do this by resetting fast pointer back to start of cycle, and moving at same pace until they're equal.
        Reset fast pointer to 0 value to guarantee it doesn't collide with any existing values (since 0 out of range).

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        fast = nums[nums[0]]
        slow = nums[0]

        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]

        fast = 0

        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow
