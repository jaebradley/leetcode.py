from unittest import TestCase


from tree_node import TreeNode
from path_sum_3 import Solution


class TestEmptyTree(TestCase):
    def test_when_sum_is_zero(self):
        self.assertEqual(0, Solution().pathSum(None, 0))


class TestSingleMatchingNode(TestCase):
    def test_when_only_root_matches(self):
        root = TreeNode(1)
        self.assertEqual(1, Solution().pathSum(root, 1))

    def test_when_only_left_child_matches(self):
        root = TreeNode(-10)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(1, Solution().pathSum(root, 1))

    def test_when_only_right_child_matches(self):
        root = TreeNode(-10)
        root.left = TreeNode(2)
        root.right = TreeNode(1)
        self.assertEqual(1, Solution().pathSum(root, 1))


class TestZeroInPath(TestCase):
    def test_when_only_left_child_matches(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(2, Solution().pathSum(root, 1))

    def test_when_only_right_child_matches(self):
        root = TreeNode(0)
        root.left = TreeNode(2)
        root.right = TreeNode(1)
        self.assertEqual(2, Solution().pathSum(root, 1))


class TestNegativeNumber(TestCase):
    def test_when_only_left_child_matches(self):
        root = TreeNode(-1)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        self.assertEqual(1, Solution().pathSum(root, 3))

    def test_when_only_right_child_matches(self):
        root = TreeNode(-1)
        root.left = TreeNode(4)
        root.right = TreeNode(1)
        self.assertEqual(1, Solution().pathSum(root, 3))


class RightSideOnly(TestCase):
    def test_right_side_sum(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        self.assertEqual(2, Solution().pathSum(root, 3))

