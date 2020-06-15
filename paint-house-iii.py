# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-192/problems/paint-house-iii/
"""

class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        MAX = 10 ** 8
        dp = [[[MAX for ___ in range(n+1)] for __ in range(target+1)] for _ in range(m)]

        # 1. no color = 0
        # 2. has color -> [1, n]
        # 3. cost[i][j] = House[i] Paint Color[j+1]

        # Init House[0]

        # Painted House Don't Need Paint Again
        if houses[0] > 0:
            dp[0][1][houses[0]] = 0
        else:
            for k in range(1, n + 1):
                dp[0][1][k] = cost[0][k - 1]

        # House -> 1 to m-1
        for i in range(1, m):
            # Target -> 1 to Target
            for j in range(1, target+1):
                # House[i] Has Color Or Not
                if houses[i] > 0:
                    # House[i] Has Color, Then Don't Need Paint House[i], Select Pre House Color as K
                    for k in range(1, n+1):
                        if k == houses[i]:
                            # Duplicate Color
                            dp[i][j][houses[i]] = min(dp[i][j][houses[i]], dp[i-1][j][k])
                        else:
                            # Other Color
                            dp[i][j][houses[i]] = min(dp[i][j][houses[i]], dp[i-1][j-1][k])
                else:
                    # House[i] No Color, Then Paint House[i]
                    # Select Current House Color as K
                    for k in range(1, n+1):
                        # Select Pre House Color as Z
                        for z in range(1, n+1):
                            if k == z:
                                # House[i] == House[j]
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][z] + cost[i][k-1])
                            else:
                                # House[i] != House[j]
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][z] + cost[i][k-1])

        rs = min(dp[m-1][target])
        if rs == MAX:
            return -1
        return rs


if __name__ == '__main__':
    assert Solution().minCost([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3) == 9
    assert Solution().minCost([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3) == 11
    assert Solution().minCost([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3) == -1