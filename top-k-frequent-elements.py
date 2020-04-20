# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Analysis:
1. use Counter in collections of python
2. use sorted function

or
1. use hashdict to record counter
2. use a max heaq to get top k
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return None
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        top_k_items = sorted(d.items(), key=lambda x:x[1], reverse=True)[:k]
        return [_[0] for _ in top_k_items]

    def topKFrequent2(self, nums, k):
        if not nums:
            return None
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        top_d = {}
        for key, val in d.items():
            if val not in top_d:
                top_d[val] = []
            top_d[val].append(key)
        sorted_top_keys = sorted(top_d.keys(), reverse=True)
        top_k = []
        for key in sorted_top_keys:
            if len(top_k) == k:
                return top_k
            for val in top_d[key]:
                if len(top_k) == k:
                    return top_k
                top_k.append(val)
        return top_k

if __name__ == '__main__':
    print Solution().topKFrequent2([1,1,1,2,2,3], 2)
    print Solution().topKFrequent2([1], 1)


# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         from collections import Counter
#         return [x[0] for x in sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)[:k]]
