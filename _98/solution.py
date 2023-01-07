from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.helper(root, -float("inf"), float("inf"))

    @staticmethod
    def helper(root: Optional[TreeNode], current_min: int, current_max: int) -> bool:
        if root is None:
            return True

        if root.val >= current_max or root.val <= current_min:
            return False

        return Solution.helper(root.left, current_min, root.val) and Solution.helper(root.right, root.val, current_max)
