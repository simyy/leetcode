# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-194/problems/making-file-names-unique/
"""

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        r = start
        for i in range(1, n):
            r ^= start + 2 * i
        return r


if __name__ == '__main__':
    assert Solution().xorOperation(5, 0) == 8
    assert Solution().xorOperation(4, 3) == 8