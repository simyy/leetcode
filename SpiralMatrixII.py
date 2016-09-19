"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Analysis:
a. n = 0, return []; n = 1, renturn [1]; n = 2, renturn [[1, 2], [4, 3]];
b. n = 3 is based on n = 1, and n = 4 is based on n = 2;
c. when n add 1, it will be add a circle, which is begin with 1.
d. notice that new[x + 1][y + 1] = old[x][y] + new[1][0]


n=1  1

n=3  1  2  3
     8  9  4
     7  6  5
     
n=5  1  2  3  4  5
     16 17 18 19 6
     15 24 25 20 7
     14 23 22 21 8
     13 12 11 10 9
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n % 2 == 0:
            m = [[1, 2], [4, 3]]
            x = n / 2 - 1
        else:
            m = [[1]]
            x = n / 2

        if n == 1 or n == 2:
            return m


        for i in range(x):
            up = range(1, len(m) + 3)

            left = up[-1] + 3 * (len(m) + 1) - 1
            for row in range(len(m)):
                for col in range(len(m)):
                    m[row][col] += left

            j = up[-1] + 1
            for row in m:
                row.append(j)
                j += 1

            down = range(j + len(m) + 1, j - 1, -1)

            j = down[0] + len(m)
            for row in m:
                row.insert(0, j)
                j -= 1
            m = [up] + m + [down]
        return m
