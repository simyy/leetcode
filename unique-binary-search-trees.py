# -*- coding: utf-8 -*-

# https://leetcode.com/problems/unique-binary-search-trees/


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dp(n)

    def recusion(self, n):
        if n <= 1:
            return 1
        sum = 0
        # every root node 1 ~ n
        for i in range(1, n + 1):
            # left tree node nums: i - 1, right tree node nums: n - i
            sum += self.recusion(i - 1) * self.recusion(n - i)
        return sum

    """
    G(n)：n个节点的BST个数
    F(i, n)：以i为根节点的n个节点的BST个数
    G(n) = F(1, n) + F(2, n) + ... + F(n, n) ：1 ~ n 每一个节点作为根节点的总合即为【n个节点的BST个数】
    F(i, n) = G(i - 1) * G(n -i)：以i为根节点的BST个数是由【小于i的节点的BST】和【大于i的节点的BST】组成
    """

    def dp(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in xrange(2, n + 1):
            # G(i) = F(1, i) + F(2, i) + ... + F(i, i)
            for j in xrange(1, i + 1):
                # F(j, n) = G(j - 1) * G(n -j)
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    print Solution().numTrees(3)
    print Solution().numTrees(19)