# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Analysis:
use quick sort thought,

1. need a sorted list
2. left & right point record the two number
3. use a map={number:index_sorted_list} to record the index of all numbers
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return None
        # Init num_map to record the index of number in nums
        num_map = {}
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = []
            # Record index[i] to num_map
            num_map[nums[i]].append(i)
        # Sort numbers to use left and right pointer
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            # If lager, move left
            if sum > target:
                j -= 1
            # If less, move right
            elif sum < target:
                i += 1
            else:
                return [num_map[nums[i]].pop(0), num_map[nums[j]].pop(0)]
        return None


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
    print s.twoSum([3, 2, 4], 6)
    print s.twoSum([3, 3], 6)
