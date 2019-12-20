# -*- coding: utf-8 -*-


# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

"""
重复数字的问题：
1. 去除重复后，等于队列迁移
2. 为了不使用额外空间，使用队列移动的方式
3. 由于重复个数不超过2个，则从2开始遍历
4. 每个数字只需要比较：当前数字是不是大于两个之前的数字（由于数字一直往左移动，
    只可能填充更大的数字），如果大于，则满足规则，如果相同，则不考虑当前值
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i



        # 理解错了题意，下面是计算出现第一个不重复的位置

        # if not nums:
        #     return None
        # if len(nums) == 1:
        #     return 0
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     elif i + 1 < len(nums) and nums[i] == nums[i + 1]:
        #         return self.removeDuplicates(nums[i:]) + i
        #     else:
        #         return i
        # return None



if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print nums, s.removeDuplicates(nums), nums
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print nums, s.removeDuplicates(nums), nums
