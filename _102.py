from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []

        queue = deque([root])

        while 0 < len(queue):
            current_size = len(queue)
            current_level_values = []

            for _ in range(current_size):
                current_element = queue.popleft()
                if None is not current_element:
                    queue.append(current_element.left)
                    queue.append(current_element.right)

                    current_level_values.append(current_element.val)

            if 0 < len(current_level_values):
                values.append(current_level_values)

        return values
