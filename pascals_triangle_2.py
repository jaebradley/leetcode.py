from typing import List

"""
https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space

Approach:

1. can store previous row in an array, start with [1]
2. for value in previous array, if value is not last value in array, sum the value with the next value and put into 
new array
3. add 1 to beginning and end of new array
4. set new array as previous row
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        previous_row = [1]

        for i in range(rowIndex):
            new_row = []
            for previous_row_index in range(len(previous_row) - 1):
                new_row.append(previous_row[previous_row_index] + previous_row[previous_row_index + 1])

            new_row.append(1)
            new_row.insert(0, 1)
            previous_row = new_row

        return previous_row
