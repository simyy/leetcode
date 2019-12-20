"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Analysis:
To solution it, must to implement a binaryToInt and intToBInary function, then use add function to calcuate.
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def b2i(b):
            if len(b) == 0:
                return 0
            sum = 0
            for i in range(0, len(b) - 1):
                sum = (sum + int(b[i])) * 2
            sum += int(b[-1])
            return sum
        def i2b(i):
            if i == 0:
                return '0'
            r = []
            while i > 0:
                if i % 2 == 1:
                    r.append('1')
                else:
                    r.append('0')
                i /= 2
            r.reverse()
            return ''.join(r)
        return i2b(b2i(a) + b2i(b))
