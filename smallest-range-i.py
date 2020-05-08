# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/smallest-range-i/
"""


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # A[i]
        MIN = min(A)
        MAX = max(A)
        # MAX - K : the minimum number in MAX numbers
        # MIN + K : the maximum number in MIN numbers
        # If [the minimum one in MAX numbers] is  lager than [the maximum one in MIN numbers],
        #   then all the value can be ZERO, so the smallest range is ZERO.
        if MAX - K <= MIN + K:
            return 0
        # Otherwise, the small range must be between
        #   [the minimum one in MAX numbers] and [the maximum one in MIN numbers].
        # Result = [the minimum one in MAX numbers] - [the maximum one in MIN numbers]
        # Result = [MAX - K] - [MIN + K] = MAX - MIN - 2 * K
        return MAX - MIN - 2 * K


if __name__ == '__main__':
    assert Solution().smallestRangeI([1], 0) == 0
    assert Solution().smallestRangeI([0, 10], 2) == 6
    assert Solution().smallestRangeI([1, 3, 6], 3) == 0