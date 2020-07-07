from typing import List

from tree_node import TreeNode

"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
Approach

* Preorder is Root, Left, Right
* Inorder is Left, Root, Right
* So preorder will tell us root node value (since it's the first value)
* Inorder will tell us the right and left subtree
* We can call buildTree recursively to build tree for left and right subtrees (with the correct
  slices of tree data)
* Can save memory by passing around references to the indices of the preorder and inorder arrays to consider
  instead of copying different parts of the same array over and over again
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = preorder[0]

        has_passed_root = False
        left_tree_inorder = []
        right_tree_inorder = []
        for element in inorder:
            if element == root:
                has_passed_root = True
            elif has_passed_root:
                right_tree_inorder.append(element)
            elif not has_passed_root:
                left_tree_inorder.append(element)

        left_tree_preorder = preorder[1:len(left_tree_inorder) + 1]
        right_tree_preorder = preorder[len(left_tree_inorder) + 1:]

        node = TreeNode(root)
        node.left = self.buildTree(preorder=left_tree_preorder, inorder=left_tree_inorder)
        node.right = self.buildTree(preorder=right_tree_preorder, inorder=right_tree_inorder)
        return node


