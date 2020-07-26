# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/contest/weekly-contest-196/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

7362981

36 98

select 36

7632981

"""

class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        arr = [int(_) for _ in num]
        from collections import defaultdict
        d = defaultdict(list)
        for i in range(len(arr)):
            d[arr[i]].append(i)

        s = 0
        while k > 0:
            if k >= len(arr[s:]) - 1:
                if len(arr[s:]) == 0:
                    break
                m = min(arr[s:])
                j = arr[s:].index(m) + s
            else:
                if len(arr[s:s+k+1]) == 0:
                    break
                m = min(arr[s:s+k+1])
                j = arr[s:s+k+1].index(m) + s
            k -= (j - s)
            while j > s:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            s += 1
        # print arr
        return "".join([str(_) for _ in arr])


if __name__ == '__main__':
    assert Solution().minInteger("4321", 4) == "1342"
    assert Solution().minInteger("100", 1) == "010"
    assert Solution().minInteger("9438957234785635408", 23) == "0345989723478563548"
    assert Solution().minInteger("36789", 1000) == "36789"
    assert Solution().minInteger("3142", 4) == "1234"
