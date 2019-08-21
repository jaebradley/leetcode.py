from unittest import TestCase

from count_complete_tree_nodes import Solution
from tree_node import TreeNode


class TestCountCompleteTreeNodes(TestCase):
    def test_count_single_level_fully_complete_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(3, Solution().countNodes(root))

    def test_empty_root(self):
        self.assertEqual(0, Solution().countNodes(None))

    def test_left_child_only(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(2, Solution().countNodes(root))

    def test_three_levels_all_but_right(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(6, Solution().countNodes(root))

    def test_three_levels_only_left_subtree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(5, Solution().countNodes(root))

    def test_three_levels_only_far_left(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(4, Solution().countNodes(root))


class TestCountCompleteTreeNodesRecursively(TestCase):
    def test_count_single_level_fully_complete_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(3, Solution().countNodesRecursive(root))

    def test_empty_root(self):
        self.assertEqual(0, Solution().countNodesRecursive(None))

    def test_left_child_only(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(2, Solution().countNodesRecursive(root))

    def test_three_levels_all_but_right(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(6, Solution().countNodesRecursive(root))

    def test_three_levels_only_left_subtree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(5, Solution().countNodesRecursive(root))

    def test_three_levels_only_far_left(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(4, Solution().countNodesRecursive(root))
