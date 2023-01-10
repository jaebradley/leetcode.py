from unittest import TestCase

from _102 import Solution, TreeNode


class TestSolution(TestCase):
    def test_level_order(self):
        self.assertListEqual(
            [
                [1],
                [2, 3]
            ],
            Solution().levelOrder(
                TreeNode(
                    val=1,
                    left=TreeNode(val=2),
                    right=TreeNode(val=3)
                )
            )
        )

        self.assertListEqual(
            [
                [1],
                [3]
            ],
            Solution().levelOrder(
                TreeNode(val=1, left=None, right=TreeNode(val=3))
            )
        )
