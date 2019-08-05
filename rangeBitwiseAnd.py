"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

Analysize:

First, the simplest method is traverse of range, but result is faild (timeout!!!).
Second,  this is a  bitwise question, which often use binary shift method, so i find below rules:

1. range(m, n) is a continue numbers.
2. m and n have a common prefix number.
3. every +1 must cause a zero on rightmost position。

so, find the common prefix, and recover shift, then will find the result.


"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # r = m
        # for i in xrange(m+1, n+1):
        #     r = r & i
        # return r
        i = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            i += 1
        return m << i
        
