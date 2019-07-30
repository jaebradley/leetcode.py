from unittest import TestCase

from merge_two_sorted_lists import Solution
from list_node import ListNode


class TestOverlapping(TestCase):
    def test_when_first_values_are_in_between_second_values_it_interweaves_two_lists(self):
        first_list = ListNode(1)
        first_list.next = ListNode(3)
        first_list.next.next = ListNode(5)

        second_list = ListNode(2)
        second_list.next = ListNode(4)
        second_list.next.next = ListNode(6)

        merged_list = ListNode(1)
        merged_list.next = ListNode(2)
        merged_list.next.next = ListNode(3)
        merged_list.next.next.next = ListNode(4)
        merged_list.next.next.next.next = ListNode(5)
        merged_list.next.next.next.next.next = ListNode(6)

        self.assertEqual(merged_list, Solution().mergeTwoLists(first_list, second_list))

    def test_when_second_values_are_in_between_first_value_it_interweaves_two_lists(self):
        second_list = ListNode(1)
        second_list.next = ListNode(3)
        second_list.next.next = ListNode(5)

        first_list = ListNode(2)
        first_list.next = ListNode(4)
        first_list.next.next = ListNode(6)

        merged_list = ListNode(1)
        merged_list.next = ListNode(2)
        merged_list.next.next = ListNode(3)
        merged_list.next.next.next = ListNode(4)
        merged_list.next.next.next.next = ListNode(5)
        merged_list.next.next.next.next.next = ListNode(6)

        self.assertEqual(merged_list, Solution().mergeTwoLists(first_list, second_list))


class TestAllIdenticalValues(TestCase):
    def test_identical_value_are_all_returned(self):
        first_list = ListNode(1)
        first_list.next = ListNode(1)
        first_list.next.next = ListNode(1)

        second_list = ListNode(1)
        second_list.next = ListNode(1)
        second_list.next.next = ListNode(1)

        merged_list = ListNode(1)
        merged_list.next = ListNode(1)
        merged_list.next.next = ListNode(1)
        merged_list.next.next.next = ListNode(1)
        merged_list.next.next.next.next = ListNode(1)
        merged_list.next.next.next.next.next = ListNode(1)

        self.assertEqual(merged_list, Solution().mergeTwoLists(first_list, second_list))


class TestNoOverlapping(TestCase):
    def test_first_list_comes_before_second_list(self):
        first_list = ListNode(1)
        first_list.next = ListNode(2)
        first_list.next.next = ListNode(3)

        second_list = ListNode(4)
        second_list.next = ListNode(5)
        second_list.next.next = ListNode(6)

        merged_list = ListNode(1)
        merged_list.next = ListNode(2)
        merged_list.next.next = ListNode(3)
        merged_list.next.next.next = ListNode(4)
        merged_list.next.next.next.next = ListNode(5)
        merged_list.next.next.next.next.next = ListNode(6)

        self.assertEqual(merged_list, Solution().mergeTwoLists(first_list, second_list))

    def test_second_list_comes_before_first_list(self):
        second_list = ListNode(1)
        second_list.next = ListNode(2)
        second_list.next.next = ListNode(3)

        first_list = ListNode(4)
        first_list.next = ListNode(5)
        first_list.next.next = ListNode(6)

        merged_list = ListNode(1)
        merged_list.next = ListNode(2)
        merged_list.next.next = ListNode(3)
        merged_list.next.next.next = ListNode(4)
        merged_list.next.next.next.next = ListNode(5)
        merged_list.next.next.next.next.next = ListNode(6)

        self.assertEqual(merged_list, Solution().mergeTwoLists(first_list, second_list))
