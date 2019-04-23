"""
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        Strategy is to keep track of ways to get to a particular cell by summing the number of values to get to the
        cell to the left of it and the ways of getting to the cell directly above it.

        If there is no cell to left or above, that value is 0.

        Sum of final cell should be all unique paths to get there.

        Should do this row by row - so do first row (since all values should be 1 since there's no cell directly above
        and only one cell to left.

        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0 or n == 0:
            return 0

        grid = []

        for x_index in range(m):
            grid.insert(x_index, [])
            row = grid[x_index]
            for y_index in range(n):
                row.insert(y_index, 0)

        grid[0][0] = 1

        for x_index in range(m):
            for y_index in range(n):
                if x_index != 0 or y_index != 0:
                    left_cell_value = 0
                    if x_index > 0:
                        left_cell_value = grid[x_index - 1][y_index]

                    above_cell_value = 0
                    if y_index > 0:
                        above_cell_value = grid[x_index][y_index - 1]

                    grid[x_index][y_index] = left_cell_value + above_cell_value

        return grid[m - 1][n - 1]


