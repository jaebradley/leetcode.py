from unittest import TestCase

from tree_node import TreeNode

from invert_binary_tree import Solution


class TestEmptyTree(TestCase):
    def setUp(self) -> None:
        self.root = None

    def test_inverted_tree_is_none(self):
        self.assertIsNone(Solution().invertTree(self.root))


class TestSingleElementTree(TestCase):
    def setUp(self) -> None:
        self.root = TreeNode(1)

    def test_inverted_tree_is_identical(self):
        self.assertEqual(Solution().invertTree(self.root), self.root)


class TestLeftChildTree(TestCase):
    def setUp(self) -> None:
        self.root = TreeNode(1)
        self.left_child = TreeNode(2)
        self.root.left = self.left_child

    def test_inverted_tree_has_right_child(self):
        expected = TreeNode(1)
        expected.right = TreeNode(2)
        self.assertEqual(Solution().invertTree(self.root), expected)


class TestRightChildTree(TestCase):
    def setUp(self) -> None:
        self.root = TreeNode(1)
        self.root.right = TreeNode(2)

    def test_inverted_tree_has_left_child(self):
        expected = TreeNode(1)
        expected.left = TreeNode(2)
        self.assertEqual(Solution().invertTree(self.root), expected)


class TestLeftAndRightChildTree(TestCase):
    def setUp(self) -> None:
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)

    def test_inverted_tree_swaps_left_and_right_children(self):
        expected = TreeNode(1)
        expected.left = TreeNode(3)
        expected.right = TreeNode(2)
        self.assertEqual(Solution().invertTree(self.root), expected)
