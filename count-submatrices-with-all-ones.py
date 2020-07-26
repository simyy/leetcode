# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/count-submatrices-with-all-ones/
"""

class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rs = 0
        row = len(mat)
        column = len(mat[0])

        memo = {}

        for i in range(row):
            for j in range(column):

                for k in range(i, row):
                    for z in range(j, column):
                        if (k, z) in memo:
                            print 'dup k=%d z=%d' % (k, z)
                            rs += 1
                            continue
                        is_valid = self.valid([i, j], [k, z], mat)
                        if is_valid:
                            # print [i, j], [k, z]
                            memo[(k, z)] = [i, j]
                            rs += 1
                        else:
                            break
        # print 'rs=', rs
        return rs



    def valid(self, f, t, mat):
        for i in range(f[0], t[0]+1):
            for j in range(f[1], t[1]+1):
                if mat[i][j] == 0:
                    return False
        return True


if __name__ == '__main__':
    mat = [[1, 0, 1],
           [1, 1, 0],
           [1, 1, 0]]
    assert Solution().numSubmat(mat) == 13
    mat = [[0, 1, 1, 0],
           [0, 1, 1, 1],
           [1, 1, 1, 0]]
    assert Solution().numSubmat(mat) == 24
    mat = [[1, 1, 1, 1, 1, 1]]
    assert Solution().numSubmat(mat) == 21
    mat = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    assert Solution().numSubmat(mat) == 5