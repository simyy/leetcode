# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Analysis:
1. Reach direction is bottom or right.
2. The matrix[0][0~n] can only have 1 possible, which only move from left.
3 The matrix[0~n][0] can only have 1 possible, which only move from top.
3. User DP solution, matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Init a matrix, DP problem, matrix[0][0~n] = 1 and matrix[0~m][0] = 1
        matrix = [[1 if i == 0 or j ==0 else 0 for j in range(n)] for i in range(m)]
        # Every path can move from left or top, then path[i][j] = path[i-1][j] + path[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[m-1][n-1]
            

if __name__ == '__main__':
    print Solution().uniquePaths(3, 2)
