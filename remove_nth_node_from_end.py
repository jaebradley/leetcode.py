"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""

from list_node import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Use two pointers.
        First pointer is used to iterate from head.
        Second pointer starts from head but only after the first pointer moves n + 1 nodes.
        When first pointer gets to end of list, second pointer should be at n + 1 nodes from end of list.
        Second pointer can now swap it's next with the next's next.
        Use dummy pointer at beginning to take into account case where remove from start.
        Runtime is O(n) since could potentially iterate through entire list in worst-case.
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        first = start
        second = start
        second.next = head

        for i in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return start.next
