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
                if tuple([x, y]) not in visited_cells:
                    search_result = self.search(x, y, visited_cells, word, board)
                    if search_result is True:
                        return True

        return False

    def search(self, x, y, visited_cells, word, board):
        if tuple([x, y]) in visited_cells:
            return False

        if len(word) == 0:
            return True

        visited_cells.add(tuple([x, y]))

        if board[y][x] != word[0]:
            return False

        if len(board[0]) - 1 > x:
            search_result = self.search(x + 1, y, visited_cells, word[1:], board)
            if search_result is True:
                return True

        if 0 < y:
            search_result = self.search(x, y - 1, visited_cells, word[1:], board)
            if search_result is True:
                return True

        if 0 < x:
            search_result = self.search(x - 1, y, visited_cells, word[1:], board)
            if search_result is True:
                return True

        if len(board) - 1 > y:
            search_result = self.search(x, y + 1, visited_cells, word[1:], board)
            if search_result is True:
                return True

        visited_cells.discard(tuple([x, y]))

        return False
