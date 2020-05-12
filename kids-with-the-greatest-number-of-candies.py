# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/biweekly-contest-25/problems/kids-with-the-greatest-number-of-candies/
"""


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        _max = max(candies)
        threshold = _max - extraCandies
        r = []
        for candy in candies:
            if candy >= threshold:
                r.append(True)
            else:
                r.append(False)
        return r

if __name__ == '__main__':
    assert Solution().kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
    assert Solution().kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False,False, False, False]
    assert Solution().kidsWithCandies([12, 1, 12], 10) == [True, False, True]
