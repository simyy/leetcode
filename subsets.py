"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# 循环迭代
class Solution1(object):
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            # 每次都会向原有列表中的list添加新值，从而生成新的list
            res += [item+[num] for item in res]
        return res

# dfs遍历
class Solution2(object):
    def dfs(self, nums, index, path, result):
        # 记录当前路径
        result.append(path)
        for i in range(index, len(nums)):
            # 探索index(已探索过得)之后每一个路径
            self.dfs(nums, i+1, path+[nums[i]], result)

    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res    

print Solution().subsets([1, 2, 3])
