# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-192/problems/the-k-strongest-values-in-an-array/
"""


class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = sorted(arr)
        index = (len(arr) - 1) / 2
        median = arr[index]

        rs = []

        i = 0
        j = len(arr) - 1

        while i <= j:
            if arr[j] - median >= median - arr[i]:
                rs.append(arr[j])
                j -= 1
            else:
                rs.append(arr[i])
                i += 1

            if len(rs) == k:
                break
        return rs




if __name__ == '__main__':
    assert Solution().getStrongest([1,1,3,5,5], 2) == [5, 5]
    assert Solution().getStrongest([6,7,11,7,6,8], 5) == [11,8,6,6,7]
    assert Solution().getStrongest([1,2,3,4,5], 2)