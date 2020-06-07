# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/4sum/
"""

# class Solution(object):
#     def fourSum(self, nums, target):
#         def findNsum(nums, target, N, result, results):
#             if len(nums) < N or target < nums[0] * N or target > nums[-1] * N:  # early termination
#                 return
#             if N == 2:  # two pointers solve sorted 2-sum problem
#                 l, r = 0, len(nums) - 1
#                 while l < r:
#                     s = nums[l] + nums[r]
#                     if s == target:
#                         results.append(result + [nums[l], nums[r]])
#                         l += 1
#                         while l < r and nums[l] == nums[l - 1]:
#                             l += 1
#                     elif s < target:
#                         l += 1
#                     else:
#                         r -= 1
#             else:  # recursively reduce N
#                 for i in range(len(nums) - N + 1):
#                     if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
#                         findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
#
#         results = []
#         findNsum(sorted(nums), target, 4, [], results)
#         return results


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def n_sum(nums, target, N, curr_nums, res_nums):
            if len(nums) < N or nums[0] * N > target or nums[-1] * N < target:
                return
            if N == 2:  # Sum 2: Use Two Pointer Shift
                l, r = 0, len(nums) - 1
                while l < r:
                    _s = nums[l] + nums[r]
                    if _s == target:
                        res_nums.append(curr_nums + [nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                    elif _s > target:
                        r -= 1
                    else:
                        l += 1
            else:  # Sum N = ((Sum 2 + nums[i]) + nums[j]) + nums[k]
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    n_sum(nums[i+1:], target - nums[i], N - 1, curr_nums + [nums[i]], res_nums)


        res_nums = []
        n_sum(sorted(nums), target, 4, [], res_nums)
        return res_nums


if __name__ == '__main__':
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    print Solution().fourSum([1,-2,-5,-4,-3,3,3,5], -11)