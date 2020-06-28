# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
"""

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = 0
        nums = sorted(nums)
        # Empty Case
        if nums[0] * 2 > target:
            return r
        # Other Case
        i, j = 0, len(nums)-1
        while i <= j:
            total = nums[i] + nums[j]
            if total <= target:
                r += 2 ** (j - i) % (10**9+7)
                i += 1
            else:
                j -= 1
        return r % (10**9+7)


if __name__ == '__main__':
    assert Solution().numSubseq([3,5,6,7], 9) == 4
    assert Solution().numSubseq([3,3,6,8], 10) == 6