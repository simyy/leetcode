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
"""
def getPermutation(self, n, k):
    array = range(1, n + 1)
    k = (k % math.factorial(n)) - 1
    permutation = []
    for i in xrange(n - 1, -1, -1):
        idx, k = divmod(k, math.factorial(i))
        permutation.append(array.pop(idx))

    return "".join(map(str, permutation))
