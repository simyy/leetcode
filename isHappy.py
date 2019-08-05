"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Analysize:

The question is a loop calcuate, the condition of happy is the result is 1, but what is the condition of unhappy?

the condition of not happy is must be the result is not equals to 1, so because of cycle calcuate, 
if the interval number is calcuated in second time then this is must a cycle calcuation,

Therefore we can find out the end condition of unhappy is a cycle calcuation; 

"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        dupSet = set()
        while True:
            n = self.calc(n)
            if n == 1:
                return True
            if n in dupSet:
                return False
            dupSet.add(n)

    def calc(self, n):
        r = 0
        while n != 0:
            r += pow(n % 10,  2)
            print r, n
            n = n / 10
        return r
