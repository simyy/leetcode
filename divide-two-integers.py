# -*- coding: utf-8 -*-

"""
# https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        x = abs(dividend)
        y = abs(divisor)

        # 32bit int -> [-2147483648, 2147483647]
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        elif divisor == -1:
            return 0 - dividend
        elif divisor == 1:
            return dividend

        # Method1: Exceed Time
        # i = 0
        # while x >= y:
        #     x -= y
        #     i += 1

        # Method2: Use shift method
        r = 0
        while x >= y:
            i = 0
            while x >= y << i:
                x -= y << i
                r += 1 << i
                i += 1

        if (dividend < 0 < divisor) or (dividend > 0 > divisor):
            return 0 - r

        return r


if __name__ == '__main__':
    # assert Solution().divide(10, 3) == 3
    # assert Solution().divide(7, -3) == -2
    # assert Solution().divide(1, 1) == 1
    assert Solution().divide(-2147483648, 1) == -2147483648
    assert Solution().divide(-2147483648, -1) == 2147483647