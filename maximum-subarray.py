# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                    dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        # print dp
        return max(dp)


if __name__ == '__main__':
    assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6