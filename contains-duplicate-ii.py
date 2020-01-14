# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Analysis:
the general solution is compare between start and start+k, but it get time limit, the time complex is o(x*k).
the best solution is that we let a dict to store all the nums, which key is the value of nums and the value of dict 
is list of index, so the value of dict is a sorted index, compare list[-1] and list[-2], if result is less then k, 
return True, otherwise return False last

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        return self.method_2(nums, k)

    def method_2(self, nums, k):
        # Init a num dict
        # key is num
        # value is a list of index
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = []
            num_dict[nums[i]].append(i)
        # Traverse num dict
        for num, array in num_dict.iteritems():
            # no equal num
            if len(array) <= 1:
                continue
            # compare index in equal num list
            for i in range(1, len(array)):
                # If the distance of i and j is at most k, return True
                if array[i] - array[i - 1] <= k:
                    return True
        return False

    # Timeout
    def method_1(self, nums, k):
        for i in range(len(nums)):
            end = i + k + 1 if i + k + 1 <= len(nums) else len(nums)
            for j in range(i + 1, end):
                if j >= len(nums):
                    break
                if nums[i] == nums[j]:
                    return True
        return False

# # Five years ago!!
# # Analysis:
# # the general solution is compare between start and start+k, but it get time limit, the time complex is o(x*k).
# # the best solution is that we let a dict to store all the nums, which key is the value of nums and the value of dict
# # is list of index, so the value of dict is a sorted index, compare list[-1] and list[-2], if result is less then k,
# #return True, otherwise return False last
# class Solution:
#     # @param {integer[]} nums
#     # @param {integer} k
#     # @return {boolean}
#     def containsNearbyDuplicate_out_limit(self, nums, k):
#         self.test(nums, k)
#         for i in range(len(nums)):
#             for j in range(1,k+1):
#                 if i + j < len(nums)  and nums[i] == nums[i + j]:
#                     return True
#         return False
#
#     def containsNearbyDuplicate(self, nums, k):
#         tmp = {}
#         for i in range(len(nums)):
#             if nums[i] not in tmp:
#                 tmp[nums[i]] = [i]
#             else:
#                 tmp[nums[i]].append(i)
#             if len(tmp[nums[i]]) >= 2 and tmp[nums[i]][-1] - tmp[nums[i]][-2] <= k:
#                 return True
#         return False


if __name__ == "__main__":
    print Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
    print Solution().containsNearbyDuplicate([1,0,1,1], 1)
    print Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2)