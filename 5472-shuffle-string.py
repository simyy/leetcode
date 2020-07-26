# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/contest/weekly-contest-199/problems/shuffle-string/
"""

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        rs = [''] * len(s)
        for i in range(len(indices)):
            rs[indices[i]] = s[i]
        return ''.join(rs)


if __name__ == '__main__':
    assert Solution().restoreString("codeleet", [4,5,6,7,0,2,1,3]) == "leetcode"
    assert Solution().restoreString("abc", [0,1,2]) == "abc"
    assert Solution().restoreString("aiohn", [3,1,4,2,0]) == "nihao"
    assert Solution().restoreString("aaiougrt", [4,0,2,6,7,3,1,5]) == "arigatou"
    assert Solution().restoreString("art", [1,0,2]) == "rat"