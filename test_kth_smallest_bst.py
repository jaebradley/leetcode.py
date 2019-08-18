from unittest import TestCase

from kth_smallest_bst import Solution
from tree_node import TreeNode


class TestKthSmallestBst(TestCase):
    def test_smallest_single_node_with_two_children(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(1, Solution().kthSmallest(root, 1))

    def test_second_smallest_single_node_with_two_children(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(2, Solution().kthSmallest(root, 2))

    def test_largest_single_node_with_two_children(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(3, Solution().kthSmallest(root, 3))


class TestKthSmallestBstRecursive(TestCase):
    def test_smallest_single_node_with_two_children(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(1, Solution().kthSmallestRecursive(root, 1))

    def test_second_smallest_single_node_with_two_children(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(2, Solution().kthSmallestRecursive(root, 2))

    def test_largest_single_node_with_two_children(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(3, Solution().kthSmallestRecursive(root, 3))