"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

Analysis:
To solute it, we must note chars in two strings.
To compare with chars in diff strings, it can only use first position to mark char.
Then, compare two char in common position of diff strings with two dict, which note every char first position.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = i
            if t[i] not in d2:
                d2[t[i]] = i
            if d1[s[i]] != d2[t[i]]:
                return False
        return True
            
