"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution(object):
    def trap(self, height):
        """
        Strategy is to calculate max height seen when traversing from right and then when traversing from left for each
        block.

        The idea is that the water at any given index is the smaller of the two max heights - the height of a block at
        that index.

        The reason to use the smaller height is that it represents the minimum "container height" whether approaching
        from the left or right.

        :type height: List[int]
        :rtype: int
        """

        max_left_height = 0
        max_right_height = 0
        max_left_heights = [0] * len(height)
        max_right_heights = [0] * len(height)

        for i in range(len(height)):
            max_left_height = max(max_left_height, height[i])
            max_left_heights[i] = max_left_height

            max_right_height = max(max_right_height, height[len(height) - 1 - i])
            max_right_heights[len(height) - 1 - i] = max_right_height

        water = 0
        for i, value in enumerate(height):
            water += min(max_left_heights[i], max_right_heights[i]) - value

        return water
