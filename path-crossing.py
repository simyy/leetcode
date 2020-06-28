# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-195/problems/path-crossing/
"""


class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x, y = 0, 0
        s = set()
        s.add("%d-%d" % (x, y))
        for p in path:

            if p == 'N':
                y += 1
            elif p == 'E':
                x += 1
            elif p == 'S':
                y -= 1
            else:
                x -= 1
            k = "%d-%d" % (x, y)
            if k in s:
                return True
            s.add(k)
        return False


if __name__ == '__main__':
    assert Solution().isPathCrossing("NES") == False
    assert Solution().isPathCrossing("NESWW") == True
    assert Solution().isPathCrossing("NNSWWEWSSESSWENNW") == True