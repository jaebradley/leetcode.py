"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        Create a heap with starting element from each row in matrix.
        Keep track of the index of each row and column index of element.
        Then, for k times, pop from the heap and if can add next element in row, push value to heap.
        Since heap is min heap, popping / pushing to heap k times should return kth smallest element.
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        result = 0
        for _ in range(k):
            result, i, j = heapq.heappop(heap)
            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return result
