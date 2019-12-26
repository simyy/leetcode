# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Analysis:
1. This is a DFS search.
2. Use a recursion loop, find every char in word.
3. Find char at the left, up, right and down neighbor.
4. Use a cache to avoid a circle path.
"""


class Solution(object):

    cached = None
    row_num = None
    column_num = None

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Marked reached node
        self.cached = set()
        self.row_num = len(board)
        self.column_num = len(board[0])
        for row in range(self.row_num):
            for column in range(self.column_num):
                if self.find_word(board, word, row, column):
                    return True
        return False

    def find_word(self, board, word, row, column):
        if not word:
            return True
        if row >= self.row_num and column >= self.column_num:
            return False
        # Current
        point = (row, column)
        if self.find_point(board, word, point):
            return True
        # Left neighbor
        point = (row, column - 1)
        if self.find_point(board, word, point):
            return True
        # Up neighbor
        point = (row - 1, column)
        if self.find_point(board, word, point):
            return True
        # Right neighbor
        point = (row, column + 1)
        if self.find_point(board, word, point):
            return True
        # Down neighbor
        point = (row + 1, column)
        if self.find_point(board, word, point):
            return True
        return False

    def find_point(self, board, word, point):
        if 0 <= point[0] < self.row_num \
                and 0 <= point[1] < self.column_num \
                and point not in self.cached \
                and board[point[0]][point[1]] == word[0]:
            self.cached.add(point)
            if self.find_word(board, word[1:], point[0], point[1]):
                return True
            self.cached.remove(point)
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    print Solution().exist(board, "ABCCED")
    print Solution().exist(board, "SEE")
    print Solution().exist(board, "ABCB")

    # board = [['a']]
    # print Solution().exist(board, "a")

