# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/triangle/
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        limit = len(triangle)
        caches = {}
        def dp(i, j):
            key = '%d-%d' % (i, j)
            if key in caches:
                return caches[key]
            if i == limit - 1:
                return triangle[i][j]
            r = min(dp(i + 1, j), dp(i + 1, j + 1)) + triangle[i][j]
            caches[key] = r
            return r
        return dp(0, 0)



if __name__ == '__main__':
    assert Solution().minimumTotal([
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]]
    ) == 11