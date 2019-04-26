"""
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution(object):
    def merge(self, intervals):
        """
        The idea is to first order the list of lists by the start index.
        Then to pick the first one as the current interval.
        Then iterate through the successive intervals and update the current interval end value if the next interval
        is overlapping.
        When a non-overlapping interval is identified, add the previous current interval (which was housing all the
        prior merging) to the set of overlapping intervals.
        Use the non-overlapping interval as the basis of evaluating successive intervals.
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        overlapping_intervals = []

        if len(intervals) == 0:
            return overlapping_intervals

        intervals.sort(key=lambda interval: int(interval[0]))
        current_interval = intervals[0]

        for interval in intervals:
            if interval[0] >= current_interval[0] and interval[0] <= current_interval[1]:
                current_interval[1] = max(interval[1], current_interval[1])
            else:
                overlapping_intervals.append(current_interval)
                current_interval = interval

        overlapping_intervals.append(current_interval)

        return overlapping_intervals
