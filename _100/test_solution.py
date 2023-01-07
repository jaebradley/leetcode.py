from unittest import TestCase

from _100.solution import Solution, TreeNode


class TestSolution(TestCase):
    def test_is_same_tree(self):
        self.assertTrue(Solution().isSameTree(p=None, q=None))
        self.assertFalse(Solution().isSameTree(p=None, q=TreeNode(val=10)))
        self.assertFalse(Solution().isSameTree(p=TreeNode(val=10), q=None))
        self.assertTrue(Solution().isSameTree(p=TreeNode(val=10), q=TreeNode(val=10)))
        self.assertFalse(Solution().isSameTree(p=TreeNode(val=11), q=TreeNode(val=10)))
        self.assertFalse(Solution().isSameTree(p=TreeNode(val=10), q=TreeNode(val=11)))
        self.assertTrue(Solution().isSameTree(p=TreeNode(val=10, left=TreeNode(val=9)), q=TreeNode(val=10, left=TreeNode(val=9))))
        self.assertFalse(
            Solution().isSameTree(p=TreeNode(val=10, left=TreeNode(val=9)), q=TreeNode(val=10, left=TreeNode(val=11))))
        self.assertTrue(
            Solution().isSameTree(p=TreeNode(val=10, left=TreeNode(val=9), right=TreeNode(val=11)), q=TreeNode(val=10, left=TreeNode(val=9), right=TreeNode(val=11))))
