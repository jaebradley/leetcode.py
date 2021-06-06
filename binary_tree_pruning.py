from tree_node import TreeNode
"""
https://leetcode.com/problems/binary-tree-pruning/

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.



Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]


Constraints:

The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.

Solution:

1. Method called no_child_contains_a_1 that takes a node
2. If node is None, return True.
   If node value is 1, return False.
   For each of node's children, call method recursively.
   If result of method call is False, set that child to None
3. Return root

"""


class Solution:
    @staticmethod
    def subtree_contains_only_zeroes(root: TreeNode):
        if root is None:
            return True

        every_left_child_is_a_zero = Solution.subtree_contains_only_zeroes(root.left)

        if every_left_child_is_a_zero is True:
            root.left = None

        every_right_child_is_a_zero = Solution.subtree_contains_only_zeroes(root.right)

        if every_right_child_is_a_zero is True:
            root.right = None

        return root.val == 0 and every_left_child_is_a_zero and every_right_child_is_a_zero

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if Solution.subtree_contains_only_zeroes(root) is True:
            return None
        return root
