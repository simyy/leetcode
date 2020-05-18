# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = sum(nums) / 2

        dp = [[False] * (target + 1) for _ in range(len(nums))]
        dp[0][0] = True
        for j in range(1, target + 1):
            if nums[0] == j:
                dp[0][j] = True

        for i in range(1, len(nums)):
            for j in range(target+1):
                if j == nums[i]:
                    dp[i][j] = True
                elif j > nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    # assert Solution().canPartition([1, 5, 11, 5]) == True
    assert Solution().canPartition([1, 2, 3, 5]) == False