# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/contest/weekly-contest-199/problems/bulb-switcher-iv/
"""

# class Solution(object):
#     def minFlips(self, target):
#         """
#         :type target: str
#         :rtype: int
#         """
#         rs = 0
#         target = int(target, 2)
#         while target != 0:
#             # 找到反转点
#             t = target % 2
#             tmp = target
#             r = 0
#             while tmp % 2 == t:
#                 tmp = tmp >> 1
#                 r += 1
#             # 反转一次
#             rs += 1
#             target = tmp
#             tt = 0 if t == 1 else 1
#             while r > 0:
#                 target = target << 1 | tt
#                 r -= 1
#         return rs


# class Solution(object):
#     def minFlips(self, target):
#         """
#         :type target: str
#         :rtype: int
#         """
#         rs = 0
#         target = int(target, 2)
#         while target > 0:
#
#             if target % 2 == 1:
#                 while target % 2 == 1:
#                     target = target >> 1
#             else:
#                 while target % 2 == 0:
#                     target = target >> 1
#             rs += 1
#         return rs


class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        # if int(target) == 0:
        #     return 0
        rs = 0
        i = 0
        while i < len(target):
            if int(target[len(target) - 1 - i]) == 1:
                while int(target[len(target) - 1 - i]) == 1 and len(target) - 1 - i >= 0:
                    i += 1
            else:
                while int(target[len(target) - 1 - i]) == 0 and len(target) - 1 - i >= 0:
                    i += 1
                if i == len(target):
                    break
            rs += 1
        return rs


if __name__ == '__main__':
    assert Solution().minFlips("10111") == 3
    assert Solution().minFlips("101") == 3
    assert Solution().minFlips("00000") == 0
    assert Solution().minFlips("001011101") == 5