# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-188/problems/minimum-time-to-collect-all-apples-in-a-tree/
"""

import Queue

class Node:
    def __init__(self, v, has_apple=False, sub_childs=None):
        self.v = v
        self.has_apple = has_apple
        self.sub_childs = None
        self.sub_apple = False

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        # Init Mapping
        d = {}
        for edge in edges:
            if edge[0] not in d:
                d[edge[0]] = []
            d[edge[0]].append(edge[1])

        # Init Tree
        root = Node(0, hasApple[0])
        q = Queue.Queue(n)
        q.put(root)
        while not q.empty():
            node = q.get()
            if node.v in d:
                childs = d[node.v]
                node.sub_childs = []
                for child in childs:
                    child_node = Node(child, hasApple[child])
                    node.sub_childs.append(child_node)
                    q.put(child_node)

        empty_edge = self.deep_traverse(root)
        print empty_edge
        return 2 * (len(edges) - empty_edge)

    def deep_traverse(self, node):
        if not node:
            return -1
        # Tree Root, Clear empty_edge
        if node.v == 0:
            empty_edge = 0
        # Exist apple at tree[i], then must be reach tree[i], so clear empty_edge
        elif node.has_apple:
            empty_edge = 0
        # Otherwise, may not need to reach tree[i], so empty_edge + 1
        else:
            empty_edge = 1

        child_empty_edge = 0
        if node.sub_childs:
            for child in node.sub_childs:
                tmp_empty_edge = self.deep_traverse(child)

                if child.has_apple or child.sub_apple:
                    node.sub_apple = True

                print '当前访问节点:', child.v, '\t无效边数:', tmp_empty_edge
                if tmp_empty_edge == 0:
                    print '由于访问节点:', child.v, '\t清除无效边'
                    empty_edge = 0
                if tmp_empty_edge > 0:
                    child_empty_edge += tmp_empty_edge
        if empty_edge > 0 and node.sub_apple:
            print '由于访问节点:', child.v, '\t由于子节点存在果子，清除当前无效边'
            empty_edge = 0
        print '节点:%d 无效边数:%d 当前节点是否有果子:%s 最终无效边数:%s' % (node.v, empty_edge, node.has_apple, empty_edge + child_empty_edge)
        return empty_edge + child_empty_edge





if __name__ == '__main__':
    # assert Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False, False, True, False, True, True, False]) == 8
    # assert Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False, False, True, False, False, True, False]) == 6
    # assert Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False, False, False, False, False, False, False]) == 0
    # assert Solution().minTime(5, [[0,1],[1,2],[1,3],[2,4]], [True, True, False, True, True]) == 8
    # assert Solution().minTime(5, [[0, 1], [0, 2], [1, 3], [0, 4]], [True, True, False, True, True]) == 8
    # assert Solution().minTime(7, [[0,1],[1,2],[1,3],[2,4],[4,5],[4,6]], [False,True,False,False,True,False,True]) == 8
    assert Solution().minTime(7, [[0, 1], [1, 2], [2, 3], [2, 4], [3, 5], [0, 6]], [True, False, False, False, True, False, False]) == 6
