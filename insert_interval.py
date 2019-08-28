"""
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        Add all intervals that end before new interval to result list.
        Merge all intervals that start before new interval ends.
        Add merged interval to result list.
        Add all remaining intervals to result list.

        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        results = []
        index = 0

        while intervals[index][1] < newInterval[0]:
            results.append(intervals[index])
            index += 1

        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1

        results.append(newInterval)

        while index < len(intervals):
            results.append(intervals[index])
            index += 1

        return results
