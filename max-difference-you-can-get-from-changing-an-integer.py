# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/biweekly-contest-25/problems/max-difference-you-can-get-from-changing-an-integer/
"""


class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        # The max one
        MAX = num
        for i in range(len(num_str)):
            if int(num_str[i]) == 9:
                continue
            else:
                MAX = int(num_str.replace(num_str[i], '9'))
                break
        # The min one
        MIN = num
        for i in range(len(num_str)):
            if num_str[i] == 0:
                continue
            # 首位非1，则替换为1
            if i == 0 and num_str[i] != '1':
                MIN = int(num_str.replace(num_str[i], '1'))
                break
            # 非首位非0，则替换为0
            if i > 0 and int(num_str[i]) > 0:
                tmp = int(num_str.replace(num_str[i], '0'))
                if tmp == 0 or len(str(tmp)) != len(num_str):
                    continue
                else:
                    MIN = tmp
                    break
        # print MAX, MIN
        return MAX - MIN

if __name__ == '__main__':
    # assert Solution().maxDiff(555) == 888
    # assert Solution().maxDiff(9) == 8
    # assert Solution().maxDiff(123456) == 820000
    # assert Solution().maxDiff(10000) == 80000
    # assert Solution().maxDiff(111) == 888
    assert Solution().maxDiff(1101057) == 8808050