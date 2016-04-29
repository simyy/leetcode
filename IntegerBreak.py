"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.

Analysis:
User DP method to solute it.
1. make a array which length is n + 1.
2. every one in array store the maximize product.
3. to calcuate maximize product of n, must get maximize i * max(n - i), where i is in (1 ..... n)
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        data = [0 for i in range(n + 1)]
        data[1] = 1
        for i in range(2, n + 1):
            data[i] = max([j * max(i - j, data[i - j]) for j in range(1, i)])
        return data[n]
