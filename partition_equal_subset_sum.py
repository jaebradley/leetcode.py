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
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1 or sum(nums) % 2 != 0:
            return False

        target_sum = int(sum(nums) / 2)
        visited_numbers = set()
        return self.helper(nums, visited_numbers, 0, target_sum, 0, 2)

    def helper(self, nums, visited_numbers, total_sum, target_sum, starting_index, k):
        if k == 0:
            return True

        if total_sum > target_sum:
            return False

        if total_sum == target_sum:
            return self.helper(nums, visited_numbers, 0, target_sum, k - 1, 0)

        if total_sum < target_sum:
            for index in range(starting_index, len(nums)):
                if index not in visited_numbers:
                    visited_numbers.add(index)

                    if self.helper(nums, visited_numbers, total_sum + nums[index], target_sum, k, index + 1):
                        return True

                    visited_numbers.remove(index)

        return False

