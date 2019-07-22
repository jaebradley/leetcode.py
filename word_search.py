"""
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution(object):
    def exist(self, board, word):
        """
        Iterate through board
        Each iteration is subproblem
        "At a particular coordinate, can I solve this word"
        Decrement word when solvable
        DFS
        Keep track of visited nodes
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited_cells = set()

        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if self.search(x, y, visited_cells, word, board):
                    return True

        return False

    def search(self, x, y, visited_cells, word, board):
        if tuple([x, y]) in visited_cells:
            return False

        if len(word) == 0:
            return True

        if board[y][x] == word[0] and len(word) == 1:
            return True

        if board[y][x] != word[0]:
            return False

        visited_cells.add(tuple([x, y]))

        if len(board[0]) - 1 > x and self.search(x + 1, y, visited_cells, word[1:], board):
            return True

        if 0 < y and self.search(x, y - 1, visited_cells, word[1:], board):
            return True

        if 0 < x and self.search(x - 1, y, visited_cells, word[1:], board):
            return True

        if len(board) - 1 > y and self.search(x, y + 1, visited_cells, word[1:], board):
            return True

        visited_cells.discard(tuple([x, y]))

        return False
