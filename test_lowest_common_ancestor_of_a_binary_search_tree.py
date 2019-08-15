from unittest import TestCase

from lowest_common_ancestor_of_a_binary_search_tree import Solution
from tree_node import TreeNode


class TestLCA(TestCase):
    def test_left_and_right(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(
            root,
            Solution().lowestCommonAncestor(root, TreeNode(1), TreeNode(3))
        )

    def test_current_node_and_left(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(
            root,
            Solution().lowestCommonAncestor(root, TreeNode(1), TreeNode(2))
        )

    def test_current_node_and_right(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(
            root,
            Solution().lowestCommonAncestor(root, TreeNode(3), TreeNode(2))
        )

    def test_iterate_down_left_subtree(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(10)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(3)
        self.assertEqual(
            root.left,
            Solution().lowestCommonAncestor(root, TreeNode(3), TreeNode(0))
        )

    def test_iterate_down_right_subtree(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(10)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(20)
        self.assertEqual(
            root.right,
            Solution().lowestCommonAncestor(root, TreeNode(6), TreeNode(20))
        )
