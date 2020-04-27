# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

"""


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if not cardPoints or not k:
            return 0
        if k >= len(cardPoints):
            return sum(cardPoints)

        _sum = sum(cardPoints[0:k])
        max = _sum
        i = -1
        while i >= -k:
            _sum = _sum + cardPoints[len(cardPoints) + i] - cardPoints[k + i]
            if max < _sum:
                max = _sum
            i -= 1
        return max


    def timeoutMethod(self, cardPoints, k):
        if not cardPoints or not k:
            return 0
        if k >= len(cardPoints):
            return sum(cardPoints)

        i = 0
        max = 0
        while i >= -k:
            _sum = None
            if i == 0:
                _sum = sum(cardPoints[i:k])
                # print cardPoints[i:i+k]
            elif i == -k:
                _sum = sum(cardPoints[i:])
                # print cardPoints[i:]
            else:
                _sum = sum(cardPoints[i:]) + sum(cardPoints[:k + i])
                # print cardPoints[i:], cardPoints[0:k + i]
            if max < _sum:
                max = _sum
            i -= 1
        return max



if __name__ == '__main__':
    assert Solution().maxScore([1,2,3,4,5,6,1], 3) == 12
    assert Solution().maxScore([2,2,2], 2) == 4
    assert Solution().maxScore([9,7,7,9,7,7,9], 7) == 55