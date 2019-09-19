"""
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution(object):
    def canPartition(self, nums):
        """
        The idea is that after processing each number, whether or not a value in the range of the target sum is reachable
        is a function of whether or not the value was previously reachable
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1 or sum(nums) % 2 != 0:
            return False

        target_sum = int(sum(nums) / 2)

        dp = [True] + [False] * target_sum

        for num in nums:
            dp = [
                dp[previous_sum]
                or (previous_sum >= num and dp[previous_sum - num])
                for previous_sum in range(target_sum + 1)
            ]

            if dp[target_sum]:
                return True

        return False
