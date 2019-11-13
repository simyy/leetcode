"""
Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.
"""

class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        self.matrix = [[0 for i in range(len(colsum))] for j in range(2)]

        for i in range(len(colsum)):
            if colsum[i] == 2:
                upper -= 1
                lower -= 1
                self.matrix[0][i] = 1
                self.matrix[1][i] = 1
                
        if upper < 0 or lower < 0:
            return []

        for i in range(len(colsum)):
            if colsum[i] == 1:
                if upper > 0:
                    self.matrix[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    self.matrix[1][i] = 1
                    lower -= 1
                else:
                    self.matrix = []
                    break
        
        if upper > 0 or lower > 0:
            return []

        # print rs
        return self.matrix
