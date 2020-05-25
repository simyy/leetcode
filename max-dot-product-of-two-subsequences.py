# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/max-dot-product-of-two-subsequences/
"""


class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1max, n2max, n1min, n2min = max(nums1), max(nums2), min(nums1), min(nums2)
        if n1max * n2max < 0 and n1min * n2min < 0: return max(n1max * n2min, n2max * n1min)
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if i == 1 and j == 1:
                #     dp[i][j] = nums1[i-1] * nums2[j-1]
                # else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + nums1[i-1] * nums2[j-1])
        return dp[-1][-1]


# class Solution(object):
#     def maxDotProduct(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: int
#         """
#         n, m = len(nums1), len(nums2)
#         dp = [[0] * m for _ in range(n)]
#         dp[0][0] = max(nums1) * max(nums2)
#         for i in range(1, n):
#             dp[i][0] = max(dp[i-1][0], nums1[i] * nums2[0])
#         for j in range(1, m):
#             dp[0][j] = max(dp[0][j-1], nums1[0] * nums2[j])
#         for i in range(1, n):
#             for j in range(1, m):
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + nums1[i-1] * nums2[j-1], dp[i-1][j-1])
#         print dp
#         return dp[-1][-1]


if __name__ == '__main__':
    assert Solution().maxDotProduct([2,1,-2,5], [3,0,-6]) == 18
    # assert Solution().maxDotProduct([3,-2], [2,-6,7]) == 21
    # assert Solution().maxDotProduct([-5,3,-5,-3,1], [-2,4,2,5,-5]) == 50
    assert Solution().maxDotProduct([-1, -1], [1, 1]) == -1

