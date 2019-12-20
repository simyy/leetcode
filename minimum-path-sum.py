# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-path-sum/\

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


Analysis:

DP solution:
    1. the problem of matrix path
    2. matrix[i, j] = min(matrix[i - 1, j], matrix[i, j - 1])), i < m, j < n
    3. return matrix[i, j]


"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.dp(grid)

    def dp(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    q = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    print s.minPathSum(q)
