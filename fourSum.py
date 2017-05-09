"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

class Solution(object):
    def sum(self, nums, target, tmp, result):
        print 'sum', nums, target, tmp
        if len(tmp) >= 4 and target != 0:
            return
        if target == 0 and len(tmp) == 4:
            print 'result', tmp
            if len(result) > 0 and ','.join([str(_) for _ in tmp]) == ','.join(str(_) for _ in result[-1]):
                return
            result.append(tmp[:])
            return
        if len(nums) == 0:
            return
        for i in range(0, len(nums)):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            if num <= target:
                ttmp = tmp[:]
                ttmp.append(num)
                print 'before tmp', ttmp
                self.sum(nums[i+1:], target-num, ttmp, result)
                ttmp = ttmp[:-1]
                print 'after tmp', ttmp
            else:
                break

    def fourSum(self, nums, target):
        nums = sorted(nums)
        print nums
        result = []
        self.sum(nums, target, [], result)
        return result

#nums = [1, 0, -1, 0, -2, 2]
#nums = [-1,0,1,2,-1,-4]
nums = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]
x = Solution().fourSum(nums, 0)

print 'result'
for xx in x:
    print xx
