"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.

Approach:

* BFS but keep track of "index" of each node (starting with 1)
* As BFSing, if node is not None, append to next queue, where if left of node, it's 2x previous node index and if it's
  right of node, it's 2x + 1 previous node index
* On each level of BFS, calculate width, and if greater than previous width, update
* Return width when nodes are empty
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        width = 0
        if root is None:
            return width

        queue = [{
            'index': 1,
            'node': root
        }]

        while len(queue) > 0:
            next_queue = []
            width = max(queue[len(queue) - 1]['index'] - queue[0]['index'] + 1, width)
            for index, node in enumerate(queue):
                if node['node'] is not None:
                    if node['node'].left is not None:
                        next_queue.append({
                            'index': node['index'] * 2,
                            'node': node['node'].left,
                        })

                    if node['node'].right is not None:
                        next_queue.append({
                            'index': node['index'] * 2 + 1,
                            'node': node['node'].right,
                        })
            queue = next_queue

        return width
