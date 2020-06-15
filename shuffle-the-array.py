# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-192/problems/shuffle-the-array/
"""


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i = 0
        j = n
        rs = []
        while i < n:
            rs.append(nums[i])
            rs.append(nums[j])
            i += 1
            j += 1
        return rs

if __name__ == '__main__':
    assert Solution().shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
    assert Solution().shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1]
    assert Solution().shuffle([1,1,2,2], 2) == [1,2,1,2]