from unittest import TestCase

from tree_node import TreeNode
from serialize_and_deserialize_binary_tree import Codec


class TestCodec(TestCase):
    def test_encode_empty_left_children(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(
            "1 2 3 none none 4 5 none none none none",
            Codec().serialize(root)
        )

    def test_decode_empty_left_children(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(
            root,
            Codec().deserialize("1 2 3 none none 4 5")
        )
