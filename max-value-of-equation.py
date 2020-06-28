# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/max-value-of-equation/
"""

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import deque
        queue = deque()
        queue.append(points[0])
        m = float("-inf")
        for j in range(1, len(points)):
            while queue and points[j][0] - queue[0][0] > k:
                queue.popleft()
            if queue:
                m = max(m, points[j][0] + points[j][1] + queue[0][1] - queue[0][0])
            while queue and points[j][1] - points[j][0] > queue[-1][1] - queue[-1][0]:
                queue.pop()
            queue.append(points[j])
        return m


if __name__ == '__main__':
    # assert Solution().findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]], 1) == 4
    # assert Solution().findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3) == 3
    assert Solution().findMaxValueOfEquation([[-16,15],[-7,-18],[-4,2],[1,0],[7,10],[9,-6],[14,5],[15,13],[16,-12],[20,20]], 8) == 38