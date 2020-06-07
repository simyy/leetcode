# -*- coding: utf-8 -*-

"""
https://leetcode.com/contest/weekly-contest-191/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""


# # Time Limit Exceeded
# class Solution(object):
#     def maxArea(self, h, w, horizontalCuts, verticalCuts):
#         """
#         :type h: int
#         :type w: int
#         :type horizontalCuts: List[int]
#         :type verticalCuts: List[int]
#         :rtype: int
#         """
#         rectangles = [[0, 0, h, w]]
#         for horizontal_line in horizontalCuts:
#             new_rectangles = []
#             for rectangle in rectangles:
#                 new_rectangles += self.horizontal_cut(rectangle, horizontal_line)
#             rectangles = new_rectangles
#         for vertical_line in verticalCuts:
#             new_rectangles = []
#             for rectangle in rectangles:
#                 new_rectangles += self.vertical_cut(rectangle, vertical_line)
#             rectangles = new_rectangles
#         area_list = [x[-1] * x[-2] for x in rectangles]
#         return max(area_list)
#
#     def horizontal_cut(self, rectangle, horizontal_line):
#         s = rectangle[0]
#         h = rectangle[2]
#         if horizontal_line > s and horizontal_line < s + h:
#             return [[s, rectangle[1], horizontal_line - s, rectangle[3]],
#                     [horizontal_line, rectangle[1], h - horizontal_line + s, rectangle[3]]]
#         return [rectangle]
#
#     def vertical_cut(self, rectangle, vertical_line):
#         s = rectangle[1]
#         w = rectangle[3]
#         if vertical_line > s and vertical_line < s + w:
#             return [[rectangle[0], s, rectangle[2], vertical_line - s],
#                     [rectangle[0], vertical_line, rectangle[2], w - vertical_line + s]]
#         return [rectangle]

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontal_max_space = self.max_space(horizontalCuts, h)
        vertical_max_space = self.max_space(verticalCuts, w)
        return (horizontal_max_space * vertical_max_space) % (10**9 + 7)

    def max_space(self, cuts, max_len):
        cuts = sorted(cuts)
        if 0 not in cuts:
            cuts.insert(0, 0)
        if max_len not in cuts:
            cuts.append(max_len)
        _max = cuts[1]
        for j in xrange(1, len(cuts)):
            if cuts[j] - cuts[j-1] > _max:
                _max = cuts[j] - cuts[j-1]
        return _max


if __name__ == '__main__':
    assert Solution().maxArea(5, 4, [1, 2, 4], [1, 3]) == 4
    assert Solution().maxArea(5, 4, [3, 1], [1]) == 6
    assert Solution().maxArea(5, 3, [3], [3]) == 9
    assert Solution().maxArea(6, 3, [5, 4, 1, 2, 3], [2, 1]) == 1
    assert Solution().maxArea(5, 2, [3, 1, 2], [1]) == 2