# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        # Init a array which default is prime
        primes = [True] * n
        # The number of 0 and 1 is not prime.
        primes[0] = primes[1] = False
        # Traverse 2 ~ n - 1
        for i in range(2, n):
            if primes[i]:
                # If primes[i] is prime, them i + n * i is must be not prime
                # (i + n * i) % i == 0
                for j in range(i + i, n, i):
                    primes[j] = False

        return sum(primes)

        # def countPrimes(self, n):
        #     """
        #     :type n: int
        #     :rtype: int
        #     """
        # # Analysis:
        # # find all the prime less then n, then the worse method is o(n^2), which should get (1..n/2)*(1...n/2).
        # # The best method is o(nlogn) time complex, which method is that i * (2...n) is not prime, then only to Traversal 2~n/2
        # if n < 3:
        #     return 0
        # # Init a array which default is prime
        # primes = [True] * n
        # # The number of 0 and 1 is not prime.
        # primes[0] = primes[1] = False
        # for i in range(2, int(n ** 0.5) + 1):
        #     if primes[i]:
        #         primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        # return sum(primes)


if __name__ == '__main__':
    print Solution().countPrimes(10)