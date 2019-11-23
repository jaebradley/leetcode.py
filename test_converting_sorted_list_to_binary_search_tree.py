from unittest import TestCase
from tree_node import TreeNode
from list_node import ListNode

from converting_sorted_list_to_binary_search_tree import Solution

class TestConvertingSortedListToBinarySearchTree(TestCase):
    def test_empty_list_results_in_empty_tree(self):
        self.assertIsNone(Solution().sortedListToBST(None))

    def test_single_list_results_in_single_tree(self):
        tree = Solution().sortedListToBST(ListNode(1))
        self.assertEqual(tree.val, 1)
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)

    def test_two_node_list_results_in_tree_with_root_and_child(self):
        list = ListNode(1)
        list.next = ListNode(2)

        tree = Solution().sortedListToBST(list)
        self.assertEqual(tree.val, 1)
        self.assertIsNone(tree.left)
        self.assertEqual(tree.right.val, 2)

    def test_three_node_list_results_in_tree_with_root_and_two_children(self):
        list = ListNode(1)
        list.next = ListNode(2)
        list.next.next = ListNode(3)

        tree = Solution().sortedListToBST(list)
        self.assertEqual(tree.val, 2)
        self.assertEqual(tree.left.val, 1)
        self.assertEqual(tree.right.val, 3)
