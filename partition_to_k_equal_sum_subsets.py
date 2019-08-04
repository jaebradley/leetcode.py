"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        Implies that there are k subsets where the numbers add up to total sum / k.

        Keep track of the numbers that have been visited, and keep track of the number of subsets by decrementing k on
        each loop.

        When processing each loop, if the loop number is ever 0, return True.

        When  current sum is greater than target sum, then return False.

        When current sum is equal to target sum, then process the validity of the remaining numbers.

        This occurs when there are multiple ways of calculating the first sum (10, 10, 10 or 10, 6, 7, 7). You need to
        check the validity of the remaining numbers and how /if they sum to the target sum.

        Important to start from 0, in case there were any numbers that were passed over in previous loop.

        This is also a bit of the DP part where the next case is finding the next matching subset (i.e. k - 1) with the
        remaining unvisited numbers.

        When current sum is less than target sum, start processing numbers from start index. If number not in start
        index, add it to visited, add the visited number to the current sum, and recursively call method with updated
        current sum, with decremented k, and with a start index from the next value.

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        visited = set()
        target_sum = int(sum(nums) / k)

        return self.canPartition(nums, visited, 0, target_sum, k, 0)

    def canPartition(self, nums, visited, current_sum, target_sum, k, start_index):
        if k == 0:
            return True

        if current_sum > target_sum:
            return False

        if current_sum == target_sum:
            return self.canPartition(nums, visited, 0, target_sum, k - 1, 0)

        if current_sum < target_sum:
            for index in range(start_index, len(nums)):
                if index not in visited:
                    visited.add(index)

                    if self.canPartition(nums, visited, current_sum + nums[index], target_sum, k, index + 1):
                        return True

                    visited.remove(index)

        return False
