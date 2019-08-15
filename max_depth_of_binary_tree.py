"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        The depth for node A is really the max of the depth of it's left child and it's right child.
        And the max depth of it's left child is really the max of the depth of the left child's children.
        So can use recursion to iterate through children and calculate max.

        Every node is visited once, so runtime is O(n).
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, node, count):
        if node is None:
            return count

        return max(
            self.helper(node.left, count + 1),
            self.helper(node.right, count + 1),
        )
