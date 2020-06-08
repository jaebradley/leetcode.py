from typing import List

"""
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

Approach:

* Think of each node in grid as node in graph
* Need to identify all 1s connected to a given 1
* So DFS from the first 1 found and find any connected 1s
* Need to take into account borders (ensure x and y coordinates are valid)
* When a 1 is found, replace with a # - this is a quick and dirty way of validating that a node was visited before
* Iterate through all nodes - if a node is found that is a 1, dfs for other 1s on that node
* This should replace all associated 1s with #s
* Increment island count as this indicates an island was found
* Continue iterating through all x and y combinations dfs-ing when a 1 is found
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        if grid:
            height = len(grid)
            width = len(grid[0])

            for y in range(height):
                for x in range(width):
                    if grid[y][x] == "1":
                        islands += 1
                        self.dfs(x, y, grid)

        return islands

    def dfs(self, x: int, y: int, grid: List[List[str]]):
        if grid[y][x] == "1":
            grid[y][x] = "#"

            if x > 0:
                self.dfs(x - 1, y, grid)

            if y > 0:
                self.dfs(x, y - 1, grid)

            if x < len(grid[y]) - 1:
                self.dfs(x + 1, y, grid)

            if y < len(grid) - 1:
                self.dfs(x, y + 1, grid)

