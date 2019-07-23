from unittest import TestCase
from reverse_linked_list import Solution
from list_node import ListNode


class TestMultipleValuesSolution(TestCase):
    def test_reverse_multiple_values(self):
        values = ListNode(1)
        values.next = ListNode(2)
        values.next.next = ListNode(3)
        values.next.next.next = ListNode(4)
        values.next.next.next.next = ListNode(5)

        expected = ListNode(5)
        expected.next = ListNode(4)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(1)

        self.assertEqual(expected, Solution().reverseList(values))

    def test_reverse2_multiple_values(self):
        values = ListNode(1)
        values.next = ListNode(2)
        values.next.next = ListNode(3)
        values.next.next.next = ListNode(4)
        values.next.next.next.next = ListNode(5)

        expected = ListNode(5)
        expected.next = ListNode(4)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(1)

        self.assertEqual(expected, Solution().reverseList2(values))


class TestEmptyListSolution(TestCase):
    def test_reverse_empty_list(self):
        self.assertIsNone(Solution().reverseList(None))

    def test_reverse2_empty_list(self):
        self.assertIsNone(Solution().reverseList2(None))


class TestSingleValueListSolution(TestCase):
    def test_reverse_single_value_list(self):
        values = ListNode(1)
        self.assertEqual(values, Solution().reverseList(values))

    def test_reverse2_single_value_list(self):
        values = ListNode(1)
        self.assertEqual(values, Solution().reverseList2(values))
