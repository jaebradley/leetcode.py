"""
https://leetcode.com/problems/max-area-of-island/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return 0

        height = len(grid)
        if height is 0:
            return 0

        self.max_area = 0
        self.visited = set()

        width = len(grid[0])

        for x in range(width):
            for y in range(height):
                self.dfs(grid, x, y, 0)

        return self.max_area

    def dfs(self, grid, x, y, count):
        if (x, y) in self.visited or grid[y][x] == 0:
            return count

        self.visited.add((x, y))

        count += 1

        self.max_area = max(self.max_area, count)

        if y > 0:
            count = self.dfs(grid, x, y - 1, count)

        if x > 0:
            count = self.dfs(grid, x - 1, y, count)

        if y < len(grid) - 1:
            count = self.dfs(grid, x, y + 1, count)

        if x < len(grid[y]) - 1:
            count = self.dfs(grid, x + 1, y, count)

        return count
