"""
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

from list_node import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        Based on values, while the first and second lists have both not been iterated through, whichever node has the
        lowest value add it to the merged list.

        If nodes have equal value, add the node from the first list.

        If the first or second list has been iterated through, iterate through the first list, if possible, then iterate
        through the second list if possible.

        Runtime is O(n + m) where n is the size of the first list and m is the size of the second list since need to
        iterate through all values.
        
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = l1
        second = l2
        merged = ListNode(0)
        current_node = merged

        while first is not None and second is not None:
            if first.val > second.val:
                current_node.next = second
                second = second.next
                current_node = current_node.next
            else:
                current_node.next = first
                first = first.next
                current_node = current_node.next

        while first is not None:
            current_node.next = first
            first = first.next
            current_node = current_node.next

        while second is not None:
            current_node.next = second
            second = second.next
            current_node = current_node.next

        return merged.next
