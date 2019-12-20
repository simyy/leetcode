# -*- coding: utf-8 -*-

# https://leetcode.com/problems/minimum-window-substring/



import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        if len(s) == 0:
            return ""
        markedI = None
        markedJ = None
        counter = collections.Counter(t)
        i = 0
        while i < len(s):
            # find first char in counter
            if s[i] in counter:
                break
            i += 1
        j = i
        while j < len(s):
            # t contains s[j]
            if s[j] in counter:
                counter[s[j]] -= 1
            # if sub(i, j) contains t, mark it, and move i
            # the reason for while is that situation "aaab contains ab"
            while self.lowerThanZero(counter):
                # init marked or min range
                if markedI is None or j - i < markedJ - markedI:
                    markedI = i
                    markedJ = j
                 # counter must be contains s[i]
                counter[s[i]] += 1
                i += 1
                while i <= j:
                    # reach next contains char, break, move j
                    if s[i] in counter:
                        break
                    else:
                        i += 1
            # move j
            j += 1
        if markedI is None:
            return ""
        return s[markedI:markedJ + 1]

    def lowerThanZero(self, counter):
        for val in counter.values():
            if val > 0:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.minWindow("ADOBECODEBANC", "ABC")
    print s.minWindow("a", "aa")
    print s.minWindow("a", "b")
    print s.minWindow("ab", "b")
    print s.minWindow("bba", "ab")












if __name__ == '__main__':
    pass
