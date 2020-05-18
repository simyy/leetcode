# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


if __name__ == '__main__':
    assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4