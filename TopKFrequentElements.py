"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

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
        from collections import Counter
        return [x[0] for x in sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)[:k]]
