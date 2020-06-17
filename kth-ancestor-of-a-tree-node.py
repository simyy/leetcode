# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-193
https://leetcode.com/contest/weekly-contest-193/problems/kth-ancestor-of-a-tree-node/


Least Common Ancestors (LCA) 最新公共祖先问题

二分法及倍增法

顺序搜索 -> 二分查找 -> 压缩范围（1,2,4,8,10）

"""

# Time Limit Exceed
# 利用parent做暴力搜索时间复杂度为O(n*k)
# class TreeAncestor(object):
#
#     def __init__(self, n, parent):
#         """
#         :type n: int
#         :type parent: List[int]
#         """
#         self.d = {}
#         for i in range(len(parent)):
#             self.d[i] = parent[i]
#
#     def getKthAncestor(self, node, k):
#         """
#         :type node: int
#         :type k: int
#         :rtype: int
#         """
#         p = node
#         while k > 0:
#             if p in self.d:
#                 p = self.d[p]
#                 k -= 1
#             else:
#                 break
#         if k == 0:
#             return p
#         return -1


# LCA 倍增
class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        self.cols = 20  # log(50000) < 16
        self.dp = [[-1] * self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]

        # 矩阵按照左向右推进（由于右侧依赖左侧数据）
        for j in range(1, self.cols):
            for i in range(n):
                # dp[i][j-1] == -1 意味着前一个倍增节点 i * 2^(j-1) 已经是root节点了，没办法向上找了
                if self.dp[i][j-1] != -1:
                    # dp[i][j] = dp[dp[i][j-1]][j-1]
                    # i * (2 ^ j) = [i * 2^(j-1)] * 2 ^(j-1)
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        if k == 0 or node == -1:
            return node
        # POS is the position closest to the k

        pos = 0
        # dp[i] 是节点i的倍增队列，第一列是i本身，后面为i * 2, i * 4, i * 6 ....
        i = 1
        while i * 2 < k and pos < len(self.dp[node]):
            i = i * 2
            pos += 1
        # dp[node][pos]为以node为起点最近k的倍增节点
        # 以dp[node][pos]为起点，再找到k-i的根节点
        return self.getKthAncestor(self.dp[node][pos], k - i)

if __name__ == '__main__':
    # Your TreeAncestor object will be instantiated and called as such:
    obj = TreeAncestor(7,[-1,0,0,1,1,2,2])
    print obj.getKthAncestor(3,1)
    print obj.getKthAncestor(5,2)
    print obj.getKthAncestor(6,3)

    # obj1 = TreeAncestor(5, [-1,0,0,0,3])
    # print obj1.getKthAncestor(1, 5)
    # print obj1.getKthAncestor(3, 2)
    # print obj1.getKthAncestor(0, 1)
    # print obj1.getKthAncestor(3, 1)
    # print obj1.getKthAncestor(3, 5)