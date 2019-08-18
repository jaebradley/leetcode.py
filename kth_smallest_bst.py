"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        Use a stack to go down the left side of the tree, adding the current node to the existing stack.

        When a null node is hit (so the first time, it'd be getting to far left of tree), pop the last value
        in stack and decrement counter.

        If counter is 0, return the current node value.

        Else, check the right node of the current node (as this should be next largest node).

        If this right node is null, keep popping off the stack (i.e. moving back up the tree) until counter is 0
        or can traverse right side of a node.

        Append that right child to stack and explore it's left.

        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root:
            stack.append(root)
            root = root.left
            while root is None:
                root = stack.pop()
                k -= 1

                if k == 0:
                    return root.val

                root = root.right

    def kthSmallestRecursive(self, root, k):
        """
        Idea is to get all the way to bottom left of tree and to decrement counter each time a left node
        is taken off call stack. This keeps track of the order of the nodes.

        If counter is 0, set the result to the current node and return.

        Else, process right sub-tree.
        :param root:
        :param k:
        :return:
        """
        self.counter = k
        self.result = None
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return

        self.helper(root.left)
        self.counter -= 1
        if self.counter == 0:
            self.result = root.val
            return

        self.helper(root.right)
