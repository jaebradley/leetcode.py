"""
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        paths_count = []
        for x in range(height):
            paths_count.append([])

            for y in range(width):
                paths_count[x].append([])

                if x == 0 and y == 0 and obstacleGrid[x][y] != 1:
                    paths_count[x][y] = 1
                else:
                    paths_count[x][y] = 0

        for x in range(height):
            for y in range(width):
                if not (x == 0 and y == 0) and obstacleGrid[x][y] != 1:
                    if x != 0 and obstacleGrid[x - 1][y] != 1:
                        paths_count[x][y] += paths_count[x - 1][y]

                    if y != 0 and obstacleGrid[x][y - 1] != 1:
                        paths_count[x][y] += paths_count[x][y - 1]

        return paths_count[height - 1][width - 1]
