"""
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True


class Solution(object):
    def findWords(self, board, words):
        """
        Strategy is to use a Trie to store the path of words.

        Trie uses a collection of nodes that contain a single character to map the paths for each word added to the
        trie.

        Each node in the trie has children, where each child represents a single character.

        Thus, able to build a link between parent and child that represents a word.

        This trie is leveraged by passing each child node down to each level of DFS.

        If a node happens to be the end of a word, that word is added to the found words.
        If a coordinate has already been visited, that level of DFS is exited.
        If the coordinate is out of bounds, that level of DFS is exited.
        If the coordinate is not in the node's children, that level of DFS is exited.

        Else, that coordinate is added to the list of coordinates visited, and the cells north, east, south, and west
        of the current cell are searched.
        
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        visited_coordinates = set()
        found_words = set()
        trie = Trie()

        for word in words:
            trie.insert(word)

        for y in range(len(board)):
            for x in range(len(board[y])):
                self.dfs(x, y, board, visited_coordinates, found_words, "", trie.root)

        return list(found_words)

    def dfs(self, x, y, board, visited_coordinates, found_words, path, node):
        if node.is_word:
            found_words.add(path)

        if (x, y) in visited_coordinates:
            return

        if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]):
            return

        c = board[y][x]

        if c not in node.children:
            return

        next_node = node.children[c]

        visited_coordinates.add((x, y))

        self.dfs(x, y + 1, board, visited_coordinates, found_words, path + c, next_node)
        self.dfs(x + 1, y, board, visited_coordinates, found_words, path + c, next_node)
        self.dfs(x, y - 1, board, visited_coordinates, found_words, path + c, next_node)
        self.dfs(x - 1, y, board, visited_coordinates, found_words, path + c, next_node)

        visited_coordinates.remove((x, y))
