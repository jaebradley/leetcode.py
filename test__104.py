from unittest import TestCase

from _104 import RecursiveSolution, TreeNode, NonRecursiveSolution


class TestSolution(TestCase):
    def test_recursive_max_depth(self):
        self.assertEqual(0, RecursiveSolution().maxDepth(None))
        self.assertEqual(1, RecursiveSolution().maxDepth(TreeNode(1)))
        self.assertEqual(2, RecursiveSolution().maxDepth(TreeNode(1, left=TreeNode(2))))
        self.assertEqual(2, RecursiveSolution().maxDepth(TreeNode(1, left=TreeNode(2), right=TreeNode(3))))
        self.assertEqual(3, RecursiveSolution().maxDepth(TreeNode(1, left=TreeNode(2, left=TreeNode(3)))))

    def test_non_recursive_max_depth(self):
        self.assertEqual(0, NonRecursiveSolution().maxDepth(None))
        self.assertEqual(1, NonRecursiveSolution().maxDepth(TreeNode(1)))
        self.assertEqual(2, NonRecursiveSolution().maxDepth(TreeNode(1, left=TreeNode(2))))
        self.assertEqual(2, NonRecursiveSolution().maxDepth(TreeNode(1, left=TreeNode(2), right=TreeNode(3))))
        self.assertEqual(3, NonRecursiveSolution().maxDepth(TreeNode(1, left=TreeNode(2, left=TreeNode(3)))))
