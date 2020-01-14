# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == '__main__':
    print Solution().containsDuplicate([1,2,3,1])
    print Solution().containsDuplicate([1,2,3,4])
    print Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])