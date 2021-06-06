from unittest import TestCase

from binary_tree_pruning import Solution
from tree_node import TreeNode


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_right_subtree(self):
        root = TreeNode(1)
        root.right = TreeNode(0)

        self.assertEqual(
            TreeNode(1),
            self.solution.pruneTree(root)
        )

    def test_left_subtree(self):
        root = TreeNode(1)
        root.left = TreeNode(0)

        self.assertEqual(
            TreeNode(1),
            self.solution.pruneTree(root)
        )

    def test_semi_right_subtree(self):
        root = TreeNode(1)
        root.right = TreeNode(0)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)

        expected = TreeNode(1)
        expected.right = TreeNode(0)
        expected.right.right = TreeNode(1)

        self.assertEqual(
            expected,
            self.solution.pruneTree(root)
        )

    def test_zeroes(self):
        root = TreeNode(0)
        root.right = TreeNode(0)
        root.right.right = TreeNode(0)
        root.right.left = TreeNode(0)

        self.assertIsNone(self.solution.pruneTree(root))



