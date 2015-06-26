/*
Description:
Count the number of prime numbers less than a non-negative number, n.

Analysis:
find all the prime less then n, then the worse method is o(n^2), which should get (1..n/2)*(1...n/2).
The best method is o(nlogn) time complex, which method is that i * (2...n) is not prime, then only to Traversal 2~n/2 
*/

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
