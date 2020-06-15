# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-193

https://leetcode.com/contest/weekly-contest-193/problems/running-sum-of-1d-array/
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


if __name__ == '__main__':
    assert Solution().runningSum([1,2,3,4]) == [1,3,6,10]
    assert Solution().runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert Solution().runningSum([3,1,2,10,1]) == [3,4,6,16,17]