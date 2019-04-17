"""
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        Strategy is to start at ends and work way to middle.
        In order to have a greater area, it must have a higher height than the minimum height of the ends.
        So iterate until find left or right that is greater than minimum height.
        Recalculate and set max area if find one that is greater.
        Do this until left index passes right index.
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1
        max_area = 0

        while left_index < right_index:
            minimum_height = min(height[left_index], height[right_index])
            max_area = max(max_area, minimum_height * (right_index - left_index))

            while height[left_index] <= minimum_height and left_index < right_index:
                left_index += 1

            while height[right_index] <= minimum_height and left_index < right_index:
                right_index -= 1

        return max_area
