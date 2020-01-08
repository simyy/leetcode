# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Analysis:
1. Merge sort method.
2. nums1 has enough space, then put bigger one at right of nums1.
3. Loop until one nums is empty.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1) - 1
        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            if i < 0:
                for x in range(j + 1):
                    nums1[x] = nums2[x]
                break

            if j < 0:
                break

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1



if __name__ == '__main__':
    #print Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    print Solution().merge([0], 0, [1], 1)