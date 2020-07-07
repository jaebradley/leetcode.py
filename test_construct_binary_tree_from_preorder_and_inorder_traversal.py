from unittest import TestCase

from construct_binary_tree_from_preorder_and_inorder_traversal import Solution
from tree_node import TreeNode


class TestSingleLeftNoRight(TestCase):
    def test_example(self):
        preorder = [1, 2]
        inorder = [2, 1]
        expected = TreeNode(1)
        expected.left = TreeNode(2)
        self.assertEqual(Solution().buildTree(preorder=preorder, inorder=inorder), expected)


class TestSingleLeftAndMultipleRightChildren(TestCase):
    def test_example(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected = TreeNode(3)
        expected.left = TreeNode(9)
        expected.right = TreeNode(20)
        expected.right.left = TreeNode(15)
        expected.right.right = TreeNode(7)
        self.assertEqual(Solution().buildTree(preorder=preorder, inorder=inorder), expected)
