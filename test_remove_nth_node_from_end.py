from unittest import TestCase

from list_node import ListNode
from remove_nth_node_from_end import Solution


class TestRemoveFromEnd(TestCase):
    def test_remove_from_end(self):
        start = ListNode(1)
        start.next = ListNode(2)
        start.next.next = ListNode(3)

        expected_start = ListNode(1)
        expected_start.next = ListNode(2)

        self.assertEqual(expected_start, Solution().removeNthFromEnd(start, 1))


class TestRemoveFromStart(TestCase):
    def test_remove_from_start(self):
        start = ListNode(1)
        start.next = ListNode(2)
        start.next.next = ListNode(3)

        expected_start = ListNode(2)
        expected_start.next = ListNode(3)

        self.assertEqual(expected_start, Solution().removeNthFromEnd(start, 3))


class TestRemoveFromMiddle(TestCase):
    def test_remove_from_middle(self):
        start = ListNode(1)
        start.next = ListNode(2)
        start.next.next = ListNode(3)

        expected_start = ListNode(1)
        expected_start.next = ListNode(3)

        self.assertEqual(expected_start, Solution().removeNthFromEnd(start, 2))
