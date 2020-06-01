from tree_node import TreeNode

"""
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Approach

* If leaf do nothing
* Else swap left and right references
* And recursively call method for left and right nodes
"""


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            right = root.right
            root.right = root.left
            root.left = right

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root
