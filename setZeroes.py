"""

"""

# -*- coding: utf-8 -*-

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroSet = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroSet.append([i, j])
        if len(zeroSet) > 0:
            for zero_position in zeroSet:
                i, j = zero_position[0], zero_position[1]
                for k in range(len(matrix[0])):
                    matrix[i][k] = 0
                for m in range(len(matrix)):
                    matrix[m][j] = 0
        return matrix


if __name__ == '__main__':
    s = Solution()
    m = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    print s.setZeroes(m)
