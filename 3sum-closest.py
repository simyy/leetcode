# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Analysis:
1. This is a array pointer problem.
2. like 3sum, 3sum  = num + 2sum
3. 2sum can be use left and right pointer traverse method.
4. compare and record min distance when reach target
5. return min distance
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # rtype is int
        # Record min distance
        result = nums[0] + nums[1] + nums[2]
        minDistance = abs(result - target)
        # sort nums
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
                total = nums[i] + nums[left] + nums[right]
                # reach target, return
                if total == target:
                    return total
                # less than minDistance
                if abs(total - target) < minDistance:
                    result = nums[i] + nums[left] + nums[right]
                    minDistance = abs(total - target)
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
        return result


if __name__ == '__main__':
    #print Solution().threeSumClosest([-1, 2, 1, -4], 1)
    #print Solution().threeSumClosest([0, 0, 0], 1)
    print Solution().threeSumClosest([1,1,-1,-1,3], -1)




