from tree_node import TreeNode

"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Strategy:
    * Use two pointers (fast and slow) to find middle node
        * Use a third pointer that keeps track of node before middle node
        * Need this pointer to adjust linked list node's next to point to null
        * This is so that on subsequent iteration, iteration stops at node before middle node
    * Left node is result of recursively applying function on everything from start to middle
    * Right node is result of recursively applying function on everything from middle to end
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if head == None:
            return None

        pre_slow = None
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next

        if pre_slow != None:
            pre_slow.next = None

        if slow == None:
            return None

        node = TreeNode(slow.val)

        if head != slow:
            node.left = self.sortedListToBST(head)

        node.right = self.sortedListToBST(slow.next)

        return node
