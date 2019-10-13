from unittest import TestCase

from maximum_width_of_binary_tree import Solution
from tree_node import TreeNode


class TestMaximumWidthOfBinaryTree(TestCase):
    def test_empty_tree(self):
        self.assertEqual(0, Solution().widthOfBinaryTree(None))

    def test_single_root_tree(self):
        root = TreeNode(1)
        self.assertEqual(1, Solution().widthOfBinaryTree(root))

    def test_single_root_tree_with_left_child(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(1, Solution().widthOfBinaryTree(root))

    def test_single_root_tree_with_right_child(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(1, Solution().widthOfBinaryTree(root))

    def test_single_root_tree_with_left_and_right_children(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(2, Solution().widthOfBinaryTree(root))

    def test_second_level_with_gap(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(4, Solution().widthOfBinaryTree(root))

    def test_multiple_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(2, Solution().widthOfBinaryTree(root))
