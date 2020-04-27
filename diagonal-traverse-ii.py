# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/diagonal-traverse-ii/

"""

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if j < len(nums[i]):
                    t = i + j
                    if t not in m:
                        m[t] = []
                    m[t].insert(0, nums[i][j])
        res = []
        for k in sorted(m.keys()):
            res += m[k]
        return res


class TimeOutSolution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        max_row = len(nums)
        max_column = max([len(row) for row in nums])
        n = max(max_row, max_column)
        node_list = []
        for i in range(1-n, n):
            node_list += (self.get_node_of_line(n, nums, i))
            print node_list
        return node_list


    def get_node_of_line(self, n, nums, b):
        node_list = []
        start = 0
        if b > 0:
            start = b
        for x in range(start, n):
        # for x in range(0, n):
            y = x - b
            if 0 <= y < n:
                j = x
                i = n - y - 1
                if i < len(nums) and j < len(nums[i]):
                    node_list.append(nums[i][j])
            elif y >= n:
                break
        # print node_list
        return node_list



if __name__ == '__main__':
    assert Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,4,2,7,5,3,8,6,9]
    assert Solution().findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]) == [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
    assert Solution().findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]) == [1,4,2,5,3,8,6,9,7,10,11]
    assert Solution().findDiagonalOrder([[1,2,3,4,5,6]]) == [1,2,3,4,5,6]
    assert Solution().findDiagonalOrder([[5,6,3,10],[9],[1,19],[9,9,2]]) == [5,9,6,1,3,9,19,10,9,2]