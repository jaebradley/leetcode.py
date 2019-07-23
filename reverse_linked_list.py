# Reverse a singly linked list.
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


class Solution(object):
    def reverseList(self, head):
        """
        Iterative solution that involves changing the next reference for the following node to point at current node.

        If empty list (i.e. head is None) return None.
        If single value list (i.e. head.next is None) return list
        If multiple values, use first and second variables to store references to nodes that are neighbors
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        first = head
        second = head.next
        head.next = None

        while second is not None:
            next_node = self.swap(first, second)
            first = second
            second = next_node

        return first

    def swap(self, first_node, second_node):
        if second_node is None:
            return None

        next_node = second_node.next
        second_node.next = first_node

        return next_node

    def reverseList2(self, head):
        return self.reverseList2Helper(head, None)

    def reverseList2Helper(self, head, next_head):
        """
        Recursive solution where subproblem is reversing list starting from remaining nodes.
        The reversed list is the current node swapped with reverse of all remaining nodes.
        head refers to current node and next_head refers to what will eventually be head.next.

        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return next_head

        next_node = head.next
        head.next = next_head

        return self.reverseList2Helper(next_node, head)
