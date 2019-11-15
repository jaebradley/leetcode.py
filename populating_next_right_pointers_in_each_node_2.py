from tree_link_node import Node


"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example:



Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.


Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


Strategy:

* While current node is non-null...
* Create a "dummy" node for a given "level"
* For each "level" iterate over children of current node setting the next references for each non-null node
  * After processing children of current node, next current node is the next reference from previous current node
  * These next references are set by previous level so other than root node, should refer to the node next to it
* Do this for loop until finished iterating through nodes in level (i.e. current level node is null)
* When done with a level, set the current node to be start of next level
  * This is just the dummy node's next reference, which should be the left-most child of the first node in the level
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        tree = root

        while root != None:
            level_start_placeholder = Node(0)
            current_level_node = level_start_placeholder

            while root != None:
                if root.left != None:
                    current_level_node.next = root.left
                    current_level_node = current_level_node.next

                if root.right != None:
                    current_level_node.next = root.right
                    current_level_node = current_level_node.next

                root = root.next

            root = level_start_placeholder.next

        return tree
