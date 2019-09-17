"""
https://leetcode.com/problems/unique-binary-search-trees-ii/

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Approach:

* Given a node i in 1...n, the left nodes will be 1...i - 1 and the right nodes will be i + 1...n.
* All potential trees for a given node i are all the potential left nodes at that point in time and all the potential
right nodes at that point in time
"""


from tree_node import TreeNode


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        values = []

        if start > end:
            values.append(None)
        elif start == end:
            values.append(TreeNode(start))
        else:
            for potential_starting_point in range(start, end + 1):
                potential_left_values = self.helper(start, potential_starting_point - 1)
                potential_right_values = self.helper(potential_starting_point + 1, end)
                for left in potential_left_values:
                    for right in potential_right_values:
                        starting_point = TreeNode(potential_starting_point)
                        starting_point.left = left
                        starting_point.right = right
                        values.append(starting_point)

        return values
