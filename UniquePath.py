"""
A  robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Analysis:

DP method to solute it.

"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(0)
            matrix.append(tmp)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[m-1][n-1]
            
        
