"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Analysis:
1. power of 2: 2 - 10, 4 - 100, 8 - 1000, then it must be n&(n - 1)==0
2. power of 4 must be power of 2
3. but the different between 2 and 4 is that the n - 1 (n is power of 4) must be can be divide with 3 (4 * 4 * ... * 4 * 3). 
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num & (num - 1) == 0 and num > 0 and (num - 1) % 3 == 0:
            return True
        return False
        
