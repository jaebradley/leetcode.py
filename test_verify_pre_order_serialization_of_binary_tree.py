from unittest import TestCase

from verify_pre_order_serialization_of_binary_tree import Solution

class TestVerifyPreOrderSerializationOfBinaryTree(TestCase):
    def test_no_right_node_is_invalid(self):
        self.assertFalse(Solution().isValidSerialization("1,#"))

    def test_no_left_node_children_is_invalid(self):
        self.assertFalse(Solution().isValidSerialization("1,#,2,3,#,4,5"))

    def test_non_null_left_and_right_nodes_are_valid(self):
        self.assertTrue(Solution().isValidSerialization("1,2,3,#,#,#,#"))

    def test_null_left_and_right_nodes_are_valid(self):
        self.assertTrue(Solution().isValidSerialization("1,#,#"))
