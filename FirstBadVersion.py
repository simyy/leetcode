"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Analysis:
use the method of 2 partition, then it became a recursion.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.badVersion(1, n)
    
    def badVersion(self, first, last):
        if first == last:
            return first
        elif first == last - 1:
            if isBadVersion(first):
                return first
            else:
                return last
        x = (first + last) / 2
        if isBadVersion(x):
            return self.badVersion(first, x)
        else:
            return self.badVersion(x, last)
