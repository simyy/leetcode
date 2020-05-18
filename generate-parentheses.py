# -*- coding: utf-8 -*-

"""
分类：回溯

https://leetcode.com/problems/generate-parentheses/
"""

# # TLE
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         result = []
#         self.backtracking(['('] * n + [')'] * n, [], result)
#         return result
#
#     def backtracking(self, left_list, curr_list, result):
#         if not self.valid(curr_list):
#             return
#         if len(left_list) == 0:
#             str = ''.join(curr_list[:])
#             if str not in result:
#                 result.append(str)
#             return
#         for i in range(len(left_list)):
#             self.backtracking(left_list[:i] + left_list[i+1:], curr_list + [left_list[i]], result)
#
#     @staticmethod
#     def valid(curr_list):
#         i = 0
#         for a in curr_list:
#             if a == '(':
#                 i += 1
#             else:
#                 i -= 1
#         return i >= 0

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.backtracking(n, n, [], result)
        return result

    def backtracking(self, left_n, right_n, curr_list, result):
        if not self.valid(curr_list):
            return
        if left_n == 0 and right_n == 0:
            result.append(''.join(curr_list[:]))
            return
        if left_n > 0:
            self.backtracking(left_n - 1, right_n, curr_list + ['('], result)
        if right_n > 0:
            self.backtracking(left_n, right_n - 1, curr_list + [')'], result)

    def valid(self, list):
        i = 0
        for a in list:
            if a == '(':
                i += 1
            else:
                i -= 1
        return i >= 0




if __name__ == '__main__':
    print Solution().generateParenthesis(1)
    print Solution().generateParenthesis(3)