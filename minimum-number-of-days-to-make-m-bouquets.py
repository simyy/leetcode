# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-193

https://leetcode.com/contest/weekly-contest-193/problems/minimum-number-of-days-to-make-m-bouquets/
"""

#  Time Limit Exceeded
# class Solution(object):
#     def minDays(self, bloomDay, m, k):
#         """
#         :type bloomDay: List[int]
#         :type m: int
#         :type k: int
#         :rtype: int
#         """
#         sorted_boomDay = sorted(bloomDay)
#         for i in sorted_boomDay:
#             tmp_bloomDay = [x -i if x - i > 0 else 0 for x in bloomDay]
#             _m = self.count(tmp_bloomDay, k)
#             if _m >= m:
#                 return i
#         return -1
#
#     def count(self, bloomDay, k):
#         i = 0
#         j = i + k
#         count = 0
#         while j <= len(bloomDay):
#             if self.meet(bloomDay, i, j):
#                 count += 1
#                 i = j
#                 j = i + k
#             else:
#                 i += 1
#                 j += 1
#         return count
#
#     def meet(self, bloomDay, i, j):
#         for k in range(i, j):
#             if bloomDay[k] != 0:
#                 return False
#         return True


class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if n < m * k:
            return -1

        def count(day):
            num = 0
            sum = 0
            for i in range(n):
                if num >= m:
                    break
                if bloomDay[i] <= day:
                    sum += 1
                else:
                    sum = 0
                if sum == k:
                    num += 1
                    sum = 0
            return num >= m

        days = sorted(set(bloomDay))
        l, r = 0, len(days) - 1
        while l < r:
            # Find middle day
            mid = l + (r - l) / 2
            # Compare count with m
            if count(days[mid]):
                # If count >= m, then must less than or equal to mid
                r = mid
            else:
                # If count < m, then must greater than mid
                l = mid + 1
        return days[l]


if __name__ == '__main__':
    assert Solution().minDays([1,10,3,10,2], 3, 1) == 3
    assert Solution().minDays([1,10,3,10,2], 3, 2) == -1
    assert Solution().minDays([7,7,7,7,12,7,7], 2, 3) == 12
    assert Solution().minDays([1000000000,1000000000], 1, 1) == 1000000000