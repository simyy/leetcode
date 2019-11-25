"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right



Analysis:
This is a DP problem. Diffrent of uniquePaths, there contains some obstacles in path.

Notice boundary:
1. matrix[0][0~n] and matrix[0~m][0] must be init based on obstacleGrid

    if i == 0 or j == 0:
        if obstacleGrid[i][j] == 1 \
                or (matrix[i - 1][j] == 0 and i >= 1) \
                or (matrix[i][j - 1] == 0 and j >= 1):
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1
            
2. if the end of grid is obstacle, return 0


"""

# -*- coding: utf-8 -*-

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if m > 0 else 0

        matrix = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if obstacleGrid[i][j] == 1 \
                            or (matrix[i - 1][j] == 0 and i >= 1) \
                            or (matrix[i][j - 1] == 0 and j >= 1):
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        matrix[i][j] = 0
                    else:
                        sum = 0
                        if obstacleGrid[i-1][j] == 0:
                            sum += matrix[i - 1][j]
                        if obstacleGrid[i][j - 1] == 0:
                            sum += matrix[i][j - 1]
                        matrix[i][j] = sum

        return matrix[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    m1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    m2 = [[1]]
    m3 = [[1, 0]]
    m4 = [[0, 0], [0, 1]]
    print s.uniquePathsWithObstacles(m1)
    print s.uniquePathsWithObstacles(m2)
    print s.uniquePathsWithObstacles(m3)
    print s.uniquePathsWithObstacles(m4)
