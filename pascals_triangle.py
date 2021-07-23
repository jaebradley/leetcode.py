from typing import List

"""
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

Approach:

1. Keep an array of previous calculated values (start with [1])
2. iterate over each index of previously calculated values and add the current index value with the next index value
3. Add these values to an array
4. Add a 1 to the beginning of the array and 1 to the end of the array
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if 1 == numRows:
            return [[1]]

        if 2 == numRows:
            return [[1], [1, 1]]

        previously_calculated_rows = [[1], [1, 1]]
        for i in range(numRows - 2):
            previously_calculated_row = previously_calculated_rows[len(previously_calculated_rows) - 1]
            next_row = []
            for current_index in range(len(previously_calculated_row) - 1):
                next_row.append(previously_calculated_row[current_index] + previously_calculated_row[current_index + 1])

            next_row.insert(0, 1)
            next_row.append(1)

            previously_calculated_rows.append(next_row)

        return previously_calculated_rows
