# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/constrained-subset-sum/

TODO
"""

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = []
        dp.append(0)
        for i in range(1, len(nums)):
            dp.append(nums[i])
            for j in range(max(0, i - k), i):
                dp[i] = max(dp[i], dp[j] + nums[i])
        print dp
        return max(dp)



#
# class ErrorSolution(object):
#     def constrainedSubsetSum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if k == 1:
#             return max(nums)
#         i = 0
#         _max = 0
#         while i < len(nums):
#             j = i
#             while j - i <= k and j < len(nums):
#                 _sum = max(sum(nums[i:j]), sum(nums[:i] + nums[j:]))
#                 print nums[:i], nums[i:j], nums[j:], _sum
#                 if _max < _sum:
#                     _max = _sum
#                 j += 1
#             i += 1
#         return _max


if __name__ == '__main__':
    # assert Solution().constrainedSubsetSum([10,2,-10,5,20], 2) == 37
    # assert Solution().constrainedSubsetSum([-1,-2,-3], 1) == -1
    assert Solution().constrainedSubsetSum([10,-2,-10,-5,20], 2) == 23
    # assert Solution().constrainedSubsetSum([-5266,4019,7336,-3681,-5767], 2) == 11355