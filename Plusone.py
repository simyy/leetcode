"""
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
Subscribe to see which companies asked this question
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return digits
        nStr = str(int(''.join(map(str, digits))) + 1)
        return [int(nStr[i]) for i in range(0, len(nStr))]
