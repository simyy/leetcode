# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/contest/weekly-contest-195/problems/check-if-array-pairs-are-divisible-by-k/
"""

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        # Mod every one
        arr = sorted(filter(lambda x: x % k != 0, [(num % k) for num in arr]))
        if len(arr) % 2 != 0:
            return False
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] + arr[j] != k:
                return False
            i += 1
            j -= 1
        return True





    # TLE
    def recurse(self, arr, k):
        if not arr:
            return True
        if len(arr) == 2 and (arr[0] + arr[1]) % k == 0:
            return True
        a = arr[0]
        for i in range(1, len(arr)):
            if (a + arr[i]) % k == 0:
                if self.recurse(arr[1:i] + arr[i+1:], k):
                    return True
        return False





if __name__ == '__main__':
    assert Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5) == True
    assert Solution().canArrange([1,2,3,4,5,6], 7) == True
    assert Solution().canArrange([1,2,3,4,5,6], 10) == False
    assert Solution().canArrange([-1,1,-2,2,-3,3,-4,4], 3) == True