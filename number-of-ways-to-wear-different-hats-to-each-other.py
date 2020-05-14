# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/biweekly-contest-25/problems/number-of-ways-to-wear-different-hats-to-each-other/

 Time Limit Exceeded 超时了
"""


# class Solution(object):
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
#         count = 0
#         for hat in hats[min_index]:
#             sub_hats = [_hat[:] for _hat in hats[:min_index] + hats[min_index + 1:]]
#             # 结束
#             if not sub_hats:
#                 return len(hats[min_index])
#             for sub_hat in sub_hats:
#                 if hat in sub_hat:
#                     sub_hat.remove(hat)
#             # print 'min:%d\tselect:%d\tlist:%s\tsrc:%s' % (min_index, hat, sub_hats, hats)
#             count += self.numberWays(sub_hats)
#
#         return count


class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        if not hats:
            return 0

        index_list = sorted([[i, len(hats[i])] for i in range(len(hats))], key=lambda x: x[1])
        min_index = index_list[0][0]

        # 无备选帽子，则无法继续
        if not hats[min_index]:
            return 0

        count = 0
        for hat in hats[min_index]:
            sub_hats = hats[:min_index] + hats[min_index + 1:]
            # 结束
            if not sub_hats:
                return len(hats[min_index])
            rollbacks = []
            for i in range(len(sub_hats)):
                sub_hat = sub_hats[i]
                if hat in sub_hat:
                    rollbacks.append(i)
                    sub_hat.remove(hat)
            # print 'min:%d\tselect:%d\tlist:%s\tsrc:%s' % (min_index, hat, sub_hats, hats)
            count += self.numberWays(sub_hats)

            for i in rollbacks:
                sub_hats[i].append(hat)

        return count


if __name__ == '__main__':
    assert Solution().numberWays([[3,4],[4,5],[5]]) == 1
    assert Solution().numberWays([[3,5,1],[3,5]]) == 4