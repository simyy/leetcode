# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? \
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Analysis:
1. This is a array pointer problem.
2. 3sum  = num + 2sum
3. 2sum can be use left and right pointer traverse method.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        # Invalid input
        if len(nums) < 3:
            return result
        # Sort nums
        nums = sorted(nums)
        for i in range(len(nums)):
            # Select first num
            # Skip duplicate num
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Convert 3sum = num + 2Sum
            # Use left and right pointer
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] > 0:
                    break
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return result


if __name__ == '__main__':
    print Solution().threeSum([-1,0,1,2,-1,-4])



