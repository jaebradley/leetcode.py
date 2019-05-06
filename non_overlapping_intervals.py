"""
https://leetcode.com/problems/non-overlapping-intervals/

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


Example 1:

Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.


Example 2:

Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.


Example 3:

Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        Similar to finding all non-overlapping intervals and then removing their counts from the set of all intervals.
        Sort intervals by end.
        Iterate through all intervals and then if interval is non-overlapping
          (i.e. it's start is greater or equal to end) then update the last interval end and the count of
          non-overlapping intervalsc
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 1:
            return 0

        count = 1
        intervals.sort(key=lambda interval: int(interval[1]))
        last_interval_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= last_interval_end:
                last_interval_end = interval[1]
                count += 1

        return len(intervals) - count
