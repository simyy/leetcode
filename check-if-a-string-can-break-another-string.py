# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/biweekly-contest-25/problems/check-if-a-string-can-break-another-string/
"""


class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        array1 = sorted(s1)
        array2 = sorted(s2)

        # 找到如何比较大小，以及第一个不相同的位置
        compare = 0
        compare_start = None
        for i in range(len(array1)):
            x = array1[i]
            y = array2[i]
            if x > y:
                compare = 1
            elif x < y:
                compare = -1
            if compare != 0:
                compare_start = i + 1
                break

        # 全部相同或者仅一个不同（compare_start超出范围）
        if not compare_start and compare_start >= len(s1):
            return True

        i = compare_start
        while i < len(array1):
            if compare == 1 and array1[i] >= array2[i]:
                i += 1
                continue
            elif compare == -1 and array1[i] <= array2[i]:
                i += 1
                continue
            else:
                return False

        return True


if __name__ == '__main__':
    # assert Solution().checkIfCanBreak("abc", "xya")
    # assert not Solution().checkIfCanBreak("abe", "acd")
    assert Solution().checkIfCanBreak("yopumzgd", "pamntyya")