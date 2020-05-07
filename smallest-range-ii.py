# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/smallest-range-ii/
"""


class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # Sort Elements ASC
        A = sorted(A)
        # Max Value is 10000, then R must be less than 10001
        R = 10001
        # Traverse every element,
        # 1. If A[i] + K is the largest one, A[i + n] must be -K
        # 2. For find smallest distance of element, A[i - n] must be +K (it will be close to A[i] + K)
        # 3. Compare every smallest distance to find answer
        for i in range(len(A)):
            MAX = max(A[i] + K, A[-1] - K)
            MIN = min(A[0] + K, A[i + 1] - K if i < len(A) - 1 else A[0] + K)
            R = min(R, MAX - MIN)
        return R


if __name__ == '__main__':
    assert Solution().smallestRangeII([1], 0) == 0
    assert Solution().smallestRangeII([0,10], 2) == 6
    assert Solution().smallestRangeII([1,3,6], 3) == 3