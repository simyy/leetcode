# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/biweekly-contest-25/problems/number-of-ways-to-wear-different-hats-to-each-other/
"""

# BFS
#  Time Limit Exceeded 超时了
# class Solution(object):
#
#     caches = {}
#
#     def numberWays(self, hats):
#         """
#         :type hats: List[List[int]]
#         :rtype: int
#         """
#         if not hats:
#             return 0
#
#         index_list = sorted([[i, len(hats[i])] for i in range(len(hats))], key=lambda x: x[1])
#         min_index = index_list[0][0]
#
#         # 无备选帽子，则无法继续
#         if not hats[min_index]:
#             return 0
#
#         total = 0
#         sub_hats = hats[:min_index] + hats[min_index + 1:]
#         for hat in hats[min_index]:
#             # 结束
#             if not sub_hats:
#                 return len(hats[min_index])
#             rollbacks = []
#             for i in range(len(sub_hats)):
#                 sub_hat = sub_hats[i]
#                 if hat in sub_hat:
#                     rollbacks.append(i)
#                     sub_hat.remove(hat)
#             # print 'min:%d\tselect:%d\tlist:%s\tsrc:%s' % (min_index, hat, sub_hats, hats)
#
#             key = "-".join([".".join([str(z) for z in sorted(x)]) for x in sub_hats])
#             if key not in self.caches:
#                 count = self.numberWays(sub_hats)
#                 self.caches[key] = count
#
#             total += self.caches[key]
#
#             for i in rollbacks:
#                 sub_hats[i].append(hat)
#
#         return total

# DP
# dp[i][state] = dp[i+1][state] + dp[i+1][state | (1 << j)], x <- hats[j]
class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        n = len(hats)
        memo = {}

        def dp(cur, pos):

            key = '%s-%s' % (cur, pos)
            if key in memo:
                return memo[key]

            # "pos = 011111" 代表仅最后一个人未戴帽子的状态
            if pos == (1 << n) - 1:
                return 1
            # cur代表当前分配的第i个帽子，『大于40』意味着没有可分配的帽子了
            if cur > 40:
                return 0

            # Step1. 不考虑当前帽子
            r = dp(cur + 1, pos)

            # Step2. 考虑当前帽子
            # 遍历每一个人，选择一个可以带帽子的人
            for i in range(n):
                # 可以戴帽子的第i个人，且这个人没有戴其他帽子
                if cur in hats[i] and pos & (1 << i) == 0:
                    r += dp(cur + 1, pos | (1 << i))
            r = r % (10 ** 9 + 7)
            memo[key] = r
            return r
        return dp(0, 0)




if __name__ == '__main__':
    # assert Solution().numberWays([[3,4],[4,5],[5]]) == 1
    # assert Solution().numberWays([[3,5,1],[3,5]]) == 4
    assert Solution().numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]) == 111