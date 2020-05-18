#!/usr/bin/env python
# encoding:utf-8


"""
# 回溯法

https://leetcode.com/problems/permutations/

本题考查组合问题，因此可以应用回溯法来结题。
主要思路：
1.从列表首部一次交换两组数组，需要注意循环边界（子串问题从1到len(list)）
2.记录循环次数，从而可以得到循环边界(每循环一次，边界+1，子串为[n+1:len(list)])
"""

import copy

# class Solution:
#     # @param {integer[]} nums
#     # @return {integer[][]}
#     def permute(self, nums):
#         result = []
#         self.permuteN(nums, result, 0)
#         return result
#
#     def permuteN(self, nums, result, n):
#         if n == len(nums):
#             result.append(nums)
#             return
#         for i in range(n, len(nums)):
#             if i != n and nums[i] == nums[n]:
#                 continue
#             new_nums = copy.deepcopy(nums)
#             tmp = new_nums[i]
#             new_nums[i] = new_nums[n]
#             new_nums[n] = tmp
#             self.permuteN(new_nums, result, n+1)


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(nums, [], result)
        return result

    def backtracking(self, left_nums, curr_nums, result):
        if len(left_nums) == 0:
            result.append(curr_nums[:])
            return
        for i in range(len(left_nums)):
            self.backtracking(left_nums[:i] + left_nums[i+1:], curr_nums + [left_nums[i]], result)


if __name__ == "__main__":
    print Solution().permute([1,2,3])
