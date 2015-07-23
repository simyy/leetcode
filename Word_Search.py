"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word): 
        history = set()
        m = len(board[0])
        n = len(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    history.add((i, j))
                    if self.findNext((i, j), history, 1, word, board):
                        return True
                    history.clear()
        return False

    
    def findNext(self, coord, history, next, word, board):
        if next == len(word):
            return True
        #print coord, '\tcurrent:', board[coord[0]][0][coord[1]], '\tnext:',word[next], '\thisty:', history
        m = len(board[0])
        n = len(board)
        x, y = coord
        if x-1 >= 0 and (x-1, y) not in history and board[x-1][y] == word[next]:
            next += 1
            history.add((x-1, y))
            res = self.findNext((x-1, y), history, next, word, board)
            if res == True:
                return True
            next -= 1
            history.remove((x-1, y))
        if x+1 < n and (x+1, y) not in history and board[x+1][y] == word[next]:
            next += 1
            history.add((x+1, y))
            res = self.findNext((x+1, y), history, next, word, board)
            if res == True:
                return True
            next -= 1
            history.remove((x+1, y))
        if y-1 >= 0 and (x, y-1) not in history and board[x][y-1] == word[next]:
            next += 1
            history.add((x, y-1))
            res = self.findNext((x, y-1), history, next, word, board)
            if res == True:
                return True
            next -= 1
            history.remove((x, y-1))
        if y+1 < m and (x, y+1) not in history and board[x][y+1] == word[next]:
            next += 1
            history.add((x, y+1))
            res = self.findNext((x, y+1), history, next, word, board)
            if res == True:
                return True
            next -= 1
            history.remove((x, y+1))
    
        return False
