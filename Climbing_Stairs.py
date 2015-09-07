"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Mus be care that if don't use the map, it will use more time to calcuate same result.
"""

class Solution(object):
    def __init__(self):
        self.map = {}

    def climbStairs(self, n):
        return self.traverse(n, 0)

    def traverse(self, n, i):
        if n <= 1:
            return 1 
        if n-1 in self.map:
            a = self.map[n-1]
        else:
            a = self.traverse(n-1, i) 
            self.map[n-1] = a
        if n-2 in self.map:
            b = self.map[n-2]
        else:
            b = self.traverse(n-2, i) 
            self.map[n-2] = b 
        return i + a + b
