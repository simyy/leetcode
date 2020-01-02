"""
Implement int sqrt(int x).
Compute and return the square root of x.

Analysis:
x^2 = y, then x = sqrt(y)
if a*a < y, the number less then a must not be comfortable, then if (a+1 * a+1) > y, the only comfortable is a.
"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1; right = x
        while True:
            mid = left + (right - left) / 2
            if mid > x / mid:
                right = mid - 1
            else:
                if mid + 1 > x / (mid + 1):
                    return mid
                else:
                    left = mid + 1
