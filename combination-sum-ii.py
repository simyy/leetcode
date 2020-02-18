# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sort candidates to avoid duplicate recurse
        sort_candidates = sorted(candidates)
        result = []
        # Recurse
        self.recurse(sort_candidates, target, [], result)
        return result

    def recurse(self, candidates, target, tmp_nums, result):
        # If target is 0, then tmp_nums[] is a valid combination.
        if target == 0:
            result.append(tmp_nums[:])
            return
        # If candidates is empty, then return.
        if not candidates:
            return
        # Traverse in candidates
        for i in range(len(candidates)):
            # Jump the same candidates to avoid duplicate recurse
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            # Only use the candidate less than target
            if candidates[i] <= target:
                # The candidates[i + 1:] is next candidates
                self.recurse(candidates[i + 1:], target - candidates[i], tmp_nums + [candidates[i]], result)
            else:
                break


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)