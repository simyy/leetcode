# -*- coding: utf-8 -*-

class Solution:
    def find(self, nums, num):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] == num:
                return mid
            elif nums[mid] > num:
                r = mid - 1
            else:
                l = mid + 1
        return r if nums[l] == num else -1



if __name__ == '__main__':
    print Solution().find([1,2,3,4,6,7,9], 2)
    print Solution().find([1,2,3,4,6,7,9], 9)
    print Solution().find([1,2,3,4,6,7,9], 8)
    print Solution().find([1,2,3,4,6,7,9], 5)