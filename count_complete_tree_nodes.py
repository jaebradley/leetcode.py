"""
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        Use BFS.

        Add nodes to array.
        Keep track of level.
        If a node in array is None then exit loop.
        Keep track of what index the first None occurs at.
        Total nodes should be 2 ^ N - 1 + index
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        level = 0
        nodes = [root]
        index = 0

        while len(nodes) > 0:
            next_nodes = []
            index = 0
            current_node = None

            for index, current_node in enumerate(nodes):
                index += 1
                if current_node is None:
                    break

                next_nodes.append(current_node.left)
                next_nodes.append(current_node.right)

            nodes = next_nodes

            if current_node is None:
                break

            level += 1

        return (2 ** level) - 1 + index - 1

    def countNodesRecursive(self, root):
        if root is None:
            return 0

        left_depth = self.getLeftMostNodeDepth(root.left)
        right_depth = self.getLeftMostNodeDepth(root.right)

        if left_depth == right_depth:
            return 2 ** left_depth + self.countNodesRecursive(root.right)
        else:
            return 2 ** right_depth + self.countNodesRecursive(root.left)

    def getLeftMostNodeDepth(self, root):
        if root is None:
            return 0

        return 1 + self.getLeftMostNodeDepth(root.left)



