# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-191/problems/maximum-product-of-two-elements-in-an-array/
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _nums = sorted(nums)
        print _nums, _nums[-1], _nums[-2]
        return (_nums[-1] - 1) * (_nums[-2] - 1)


if __name__ == '__main__':
    assert Solution().maxProduct([3,4,5,2]) == 12