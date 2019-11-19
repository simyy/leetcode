"""
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

5年后第二次刷该题！

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
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = []
            map[nums[i]].append(i)
            map[nums[i]].sort()
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [map[nums[i]].pop(0), map[nums[j]].pop(0)]
        return None

s = Solution()
print s.twoSum([2, 7, 11, 15], 9)
print s.twoSum([3, 2, 4], 6)
print s.twoSum([3, 3], 6)
