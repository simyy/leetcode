# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-193

https://leetcode.com/contest/weekly-contest-193/problems/least-number-of-unique-integers-after-k-removals/
"""

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
        num_count = sorted([(key, val) for key, val in d.items()], key=lambda x: x[1])
        total = len(num_count)
        # print num_count, total
        for num, count in num_count:
            if k > count:
                k -= count
                total -= 1
                continue
            elif k == count:
                k -= count
                total -= 1
                break
            else:
                break
        # print total
        return total

if __name__ == '__main__':
    assert Solution().findLeastNumOfUniqueInts([5,5,4], 1) == 1
    assert Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3) == 2