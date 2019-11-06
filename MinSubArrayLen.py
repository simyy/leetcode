"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Analysis:
1. notice: 
  contiguous array 
  subarray sum ≥ s
  
2. use two pointer left and right like slide window 

"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        left = 0
        right = 0
        sum = 0
        minLen = None
        while left < len(nums) and right < len(nums):
            while sum < s and right < len(nums):
                #print 'sum < s', sum
                sum += nums[right]
                right += 1
            while sum >= s and left < right:
                #print 'sum >= s', sum
                cLen = right - left
                if minLen is None:
                    minLen = cLen
                elif minLen > cLen:
                    minLen = cLen
                sum -= nums[left]
                left += 1
        return minLen if minLen is not None else 0
