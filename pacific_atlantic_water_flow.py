"""
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific
ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
import collections


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        Using BFS, flow "upward" from the cells in the first column (pacific), first row (pacific),
        last column (atlantic), and last row (atlantic).

        For each cell popped from the queue, evaluate the cells around it.
        For each valid cell, if it has not been added to the reachable cells for pacific or atlantic, and the cell
        value is greater than the current cell, add it to the queue and add it to reachable cells.

        Compare the reachable cells for pacific and atlantic and find set intersection.

        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix is None or len(matrix) == 0:
            return []

        max_height = len(matrix) - 1
        max_length = len(matrix[0]) - 1

        pacific_starting_coordinates = set(
            [(i, 0) for i in range(max_height + 1)] + [(0, j) for j in range(1, max_length + 1)]
        )
        atlantic_starting_coordinates = set(
            [(i, max_length) for i in range(max_height + 1)] + [(max_height, j) for j in range(max_length + 1)]
        )

        return list(
            self.bfs(matrix, pacific_starting_coordinates, max_height, max_length).intersection(
                self.bfs(matrix, atlantic_starting_coordinates, max_height, max_length)
            )
        )

    def bfs(self, matrix, reachable_cells, max_height, max_length):
        queue = collections.deque(reachable_cells)

        while queue:
            (height, length) = queue.popleft()

            for (height_diff, length_diff) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_height = height + height_diff
                next_length = length + length_diff

                if 0 <= next_height <= max_height and 0 <= next_length <= max_length \
                        and (next_height, next_length) not in reachable_cells \
                        and matrix[next_height][next_length] >= matrix[height][length]:
                    queue.append((next_height, next_length))
                    reachable_cells.add((next_height, next_length))

        return reachable_cells
