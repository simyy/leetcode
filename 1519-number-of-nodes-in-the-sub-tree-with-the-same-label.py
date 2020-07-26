# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""

# 超出时间限制
class Solution(object):
    # def countSubTrees(self, n, edges, labels):
    #     """
    #     :type n: int
    #     :type edges: List[List[int]]
    #     :type labels: str
    #     :rtype: List[int]
    #     """
    #     indegree = {}
    #     map = {}
    #     for i in range(n):
    #         indegree[i] = []
    #         map[i] = []
    #
    #     from collections import deque
    #
    #     dq = deque()
    #     dq.append(0)
    #     cache = []
    #     while dq:
    #         p = dq.pop()
    #         for i in range(len(edges)):
    #             if i in cache:
    #                 continue
    #             edge = edges[i]
    #             if edge[0] == p:
    #                 indegree[p].append(edge[1])
    #                 map[p].append(edge[1])
    #                 dq.append(edge[1])
    #                 cache.append(i)
    #             elif edge[1] == p:
    #                 indegree[p].append(edge[0])
    #                 map[p].append(edge[0])
    #                 dq.append(edge[0])
    #                 cache.append(i)
    #
    #
    #     def merge(a, b):
    #         for i in range(len(a)):
    #             a[i] += b[i]
    #
    #     d = {}
    #     while indegree:
    #         for k, v in indegree.items():
    #             if not v:
    #                 d[k] = [0] * 26
    #                 d[k][ord(labels[k]) - ord('a')] = 1
    #                 if map[k]:
    #                     for child in map[k]:
    #                         merge(d[k], d[child])
    #                 indegree.pop(k)
    #                 for k1, v1 in indegree.items():
    #                     if v1 and k in v1:
    #                         indegree[k1].remove(k)
    #     rs = []
    #     for i in range(n):
    #         rs.append(d[i][ord(labels[i]) - ord('a')])
    #     return rs

    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        rs = [1] * n

        visited = set()

        def dfs(i, edges, labels):
            arr = [0] * n
            arr[i] = 1

            for j in range(len(edges)):
                edge = edges[j]
                if edge in visited:
                    continue
                if i == edge[0] or i == edge[1]:
                    visited.add(edge)
                    child = edge[1] if i == edge[0] else edge[0]
                    arr[i] += dfs(child, edges, labels)[i]

            return arr


if __name__ == '__main__':
    assert Solution().countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd") == [2,1,1,1,1,1,1]
    assert Solution().countSubTrees(4, [[0,1],[1,2],[0,3]], "bbbb") == [4,2,1,1]
    assert Solution().countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], "aabab") == [3,2,1,1,1]
    assert Solution().countSubTrees(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], "cbabaa") == [1,2,1,1,2,1]
    assert Solution().countSubTrees(7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa") == [6,5,4,1,3,2,1]
    assert Solution().countSubTrees(4, [[0, 2], [0, 3], [1, 2]], "aeed") == [1,1,2,1]
