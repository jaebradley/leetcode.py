"""
https://leetcode.com/problems/the-skyline-problem/

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""
import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        Iterate through list of buildings.
        Collect all start points (negate the height to be used in "max heap" later).
        Collect all end points (set the first index value as the right index and the height as 0).
        Sort points.
        Initialize max heap with an initial height of 0 and an end index of infinity.
        Initialize results with [0, 0].
        For each height, pop any max heights in heap that have ended.
        Add height, if height is not 0 (aka an end point).
        If previous result's height is not equal to max heap's height, then append [index, max heap's height] to result
        list.
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        sorted_heights = [(L, -H, R) for L, R, H in buildings]
        sorted_heights += list({(R, 0, 0) for _, R, _ in buildings})
        sorted_heights.sort()

        max_heap = [(0, float("inf"))]
        results = [[0, 0]]

        for index, negative_height, right in sorted_heights:
            while index >= max_heap[0][1]:
                heapq.heappop(max_heap)
            if negative_height:
                heapq.heappush(max_heap, (negative_height, right))
            if results[-1][1] != -max_heap[0][0]:
                results.append([index, -max_heap[0][0]])

        return results[1:]
