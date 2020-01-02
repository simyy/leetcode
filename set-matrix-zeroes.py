# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_set = []
        # Add (i, j) to zero_set when matrix(i, j) == 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_set.append([i, j])
        # Traverse zero_set to set zero
        if len(zero_set) > 0:
            for point in zero_set:
                zero_row, zero_column = point[0], point[1]
                # Set all column of row[i] to 0
                for column in range(len(matrix[0])):
                    matrix[zero_row][column] = 0
                # Set all row of column[i] to 0
                for row in range(len(matrix)):
                    matrix[row][zero_column] = 0
        return matrix


if __name__ == '__main__':
    s = Solution()
    m = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    print s.setZeroes(m)
