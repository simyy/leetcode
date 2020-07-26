# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-196/problems/can-make-arithmetic-progression-from-sequence/
"""


class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        t = arr[1] - arr[0]
        i = 2
        while i < len(arr):
            if arr[i] - arr[i-1] != t:
                return False
            i += 1
        return True


if __name__ == '__main__':
    assert Solution().canMakeArithmeticProgression([3,5,1]) == True
    assert Solution().canMakeArithmeticProgression([1,2,4]) == False