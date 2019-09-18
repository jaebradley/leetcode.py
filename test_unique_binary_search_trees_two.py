from unittest import TestCase

from tree_node import TreeNode
from unique_binary_search_trees_two import Solution


class TestUniqueBinarySearchTreesTwo(TestCase):
    def test_zero(self):
        self.assertEqual(
            [None],
            Solution().generateTrees(0)
        )

    def test_one(self):
        self.assertEqual(
            [TreeNode(1)],
            Solution().generateTrees(1)
        )

    def test_two(self):
        first_tree = TreeNode(1)
        first_tree.right = TreeNode(2)

        second_tree = TreeNode(2)
        second_tree.left = TreeNode(1)
        self.assertEqual(
            [first_tree, second_tree],
            Solution().generateTrees(2)
        )
