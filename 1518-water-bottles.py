# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/water-bottles/
"""

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        nums = numBottles
        while numBottles >= numExchange:
            x = numBottles / numExchange
            nums += x
            numBottles = x + numBottles % numExchange
        return nums


if __name__ == '__main__':
    assert Solution().numWaterBottles(9, 3) == 13
    assert Solution().numWaterBottles(15, 4) == 19
    assert Solution().numWaterBottles(5, 5) == 6
    assert Solution().numWaterBottles(2, 3) == 2