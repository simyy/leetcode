"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Analysis:

N premutation = N! = N * (N-1) * (N-2) * ... * 1

Example, Given n and k, the kth permution sequence is a1 a2 a3 ... an,

let K1 = K
then a1 = K1 / (n-1)!

let K2 = K1 % (n-1)!
then a2 = K2 / (n-2)!
 .......
a(n-1) = K(n-1) / 1!
K(n-1) = K(n-2) /2!
an = K(n-1)
"""
def getPermutation(self, n, k):
    array = range(1, n + 1)
    k = (k % math.factorial(n)) - 1
    permutation = []
    for i in xrange(n - 1, -1, -1):
        idx, k = divmod(k, math.factorial(i))
        permutation.append(array.pop(idx))

    return "".join(map(str, permutation))
