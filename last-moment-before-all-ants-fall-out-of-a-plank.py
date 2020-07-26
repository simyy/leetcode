# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
"""

class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        # meet equal to switch two ants
        m = None
        if left:
            for a in left:
                if m:
                    m = max(a, m)
                else:
                    m = a
        if right:
            for b in right:
                if m:
                    m = max(n - b, m)
                else:
                    m = n - b
        return m


if __name__ == '__main__':
    # assert Solution().getLastMoment(4, [4, 3], [0, 1]) == 4
    assert Solution().getLastMoment(7, [], [0,1,2,3,4,5,6,7]) == 7
    assert Solution().getLastMoment(7, [0,1,2,3,4,5,6,7], []) == 7