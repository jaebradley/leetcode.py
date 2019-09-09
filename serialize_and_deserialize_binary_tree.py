"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree_node import TreeNode
import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        BFS through tree and append "none" when child nodes do not exist.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        nodes = [str(root.val)]
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            for child in [node.left, node.right]:
                if child:
                    nodes.append(str(child.val))
                    queue.append(child)
                else:
                    nodes.append("none")

        return " ".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        Split data on spaces.
        Root is first node.
        Iterate through nodes.
        Pop value from queue - this will be parent of next values.
        If node value for current index is not "none" then instantiate TreeNode with value and append it to queue.
        Increment index and apply same operation.
        Increment index at end of loop.
        Return root.
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        nodes = data.split(" ")
        root = TreeNode(int(nodes[0]))
        queue = collections.deque()
        queue.append(root)
        index = 1

        while queue and index < len(nodes):
            parent = queue.popleft()

            if nodes[index] != "none":
                parent.left = TreeNode(int(nodes[index]))
                queue.append(parent.left)

            index += 1

            if index < len(nodes) and nodes[index] != "none":
                parent.right = TreeNode(int(nodes[index]))
                queue.append(parent.right)

            index += 1

        return root
