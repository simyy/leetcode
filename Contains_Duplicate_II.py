"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j 
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

Analysis:
the general solution is compare between start and start+k, but it get time limit, the time complex is o(x*k).
the best solution is that we let a dict to store all the nums, which key is the value of nums and the value of dict 
is list of index, so the value of dict is a sorted index, compare list[-1] and list[-2], if result is less then k, 
return True, otherwise return False last

"""


#!/usr/bin/env python
# encoding:utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate_out_limit(self, nums, k):
        self.test(nums, k)
        for i in range(len(nums)):
            for j in range(1,k+1):
                if i + j < len(nums)  and nums[i] == nums[i + j]:
                    return True     
        return False

    def containsNearbyDuplicate(self, nums, k):
        tmp = {}
        for i in range(len(nums)):
            if nums[i] not in tmp:
                tmp[nums[i]] = [i] 
            else:
                tmp[nums[i]].append(i)
            if len(tmp[nums[i]]) >= 2 and tmp[nums[i]][-1] - tmp[nums[i]][-2] <= k:
                return True
        return False


if __name__ == "__main__":
    a = Solution()
    print a.containsNearbyDuplicate([1, 2, 3, 1], 3)
