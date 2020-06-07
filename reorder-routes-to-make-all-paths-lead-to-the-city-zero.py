# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-191/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""

from collections import deque


#  Time Limit Exceeded
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # {0: 1, 1: 3, 2: 3, 4: 5}
        roads = set()
        # {0: [1, 4], 1: [0, 3], 2: [3], 3: [1, 2], 4: [0, 5], 5: [4]}
        graph = {}
        for f, t in connections:
            roads.add((f, t))
            if f not in graph:
                graph[f] = []
            if t not in graph:
                graph[t] = []
            graph[f].append(t)
            graph[t].append(f)

        rs = 0

        queue = deque()
        queue.append(0)
        records = []

        while len(queue) != 0:
            p = queue.pop()
            records.append(p)
            if p in graph:
                for q in graph[p]:
                    if q not in records:
                        queue.append(q)
                        if (q, p) not in roads:
                            rs += 1
        return rs





if __name__ == '__main__':
    assert Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3
    assert Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]]) == 2