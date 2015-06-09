/*
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

Analysis:
本题考查组合问题，因此可以应用回溯法来结题。
主要思路：
1.从列表首部一次交换两组数组，需要注意循环边界（子串问题从1到len(list)）
2.记录循环次数，从而可以得到循环边界(每循环一次，边界+1，子串为[n+1:len(list)])
*/

#!/usr/bin/env python
# encoding:utf-8

import copy


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        result = []
        self.permuteN(nums, result, 0)
        return result
       
    def permuteN(self, nums, result, n):
        if n == len(nums):
            result.append(nums)
            return
        for i in range(n, len(nums)):
            if i != n and nums[i] == nums[n]:
                continue
            new_nums = copy.deepcopy(nums)
            tmp = new_nums[i]
            new_nums[i] = new_nums[n]
            new_nums[n] = tmp
            self.permuteN(new_nums, result, n+1)
            

if __name__ == "__main__":
    a = Solution()
    print a.permute([1,2,3])
