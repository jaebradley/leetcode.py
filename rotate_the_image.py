"""
https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution(object):
    def rotate(self, matrix):
        """
        Common method to rotate clockwise.

        1. Reverse up to down
        2. Swap the reflections (matrix[i][j] with matrix[j][i])
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.reverse(matrix)
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                current_cell = matrix[i][j]
                mirror_cell = matrix[j][i]
                matrix[i][j] = mirror_cell
                matrix[j][i] = current_cell

    def reverse(self, matrix):
        for i in range(int(len(matrix) / 2)):
            current_row = matrix[i]
            swap_row = matrix[len(matrix) - 1 - i]
            matrix[i] = swap_row
            matrix[len(matrix) - 1 - i] = current_row




