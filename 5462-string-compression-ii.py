# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/string-compression-ii/
"""

class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 压缩
        compression = s[0]
        i = 1
        while i < len(s):
            c = 1
            while s[i] == s[i-1]:
                c += 1
                i += 1
            if c > 1:
                compression += str(c) + s[i]
            else:
                compression += s[i]
            i += 1
        #


if __name__ == '__main__':
    assert Solution().getLengthOfOptimalCompression("aaabcccd", 2) == 4