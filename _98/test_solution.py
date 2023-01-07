from unittest import TestCase

from _98.solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_is_valid_bst(self):
        self.assertTrue(Solution().isValidBST(None))
        self.assertTrue(Solution().isValidBST(TreeNode()))
        self.assertTrue(Solution().isValidBST(TreeNode(val=10, left=None, right=TreeNode(11))))
        self.assertTrue(Solution().isValidBST(TreeNode(val=10, left=TreeNode(9), right=None)))
        self.assertFalse(Solution().isValidBST(TreeNode(val=2, left=TreeNode(val=2), right=TreeNode(val=2))))
        self.assertFalse(Solution().isValidBST(
            TreeNode(val=5, left=TreeNode(val=4), right=TreeNode(val=6, left=TreeNode(val=3), right=TreeNode(val=7)))))
