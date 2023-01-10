from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class NonRecursiveSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                current_element = queue.popleft()
                if current_element is not None:
                    queue.append(current_element.left)
                    queue.append(current_element.right)

            if len(queue) > 0:
                depth += 1

        return depth
