# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

# TLE
# class Solution(object):
#     def maxVowels(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         _max = 0
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         i = 0
#         j = i + k if i + k < len(s) else len(s)
#         while j <= len(s):
#             vowel_num = sum([1 for x in s[i:j] if x in vowels])
#             if vowel_num > _max:
#                 print vowel_num, s[i:j]
#                 _max = vowel_num
#             i += 1
#             j += 1
#         return _max

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        i = 0
        j = i + k - 1 if i + k - 1 < len(s) else len(s)
        pre_count = sum([1 for x in s[i:j+1] if x in vowels])
        _max = pre_count
        while j < len(s):
            i += 1
            j += 1
            if j >= len(s):
                break
            if s[i - 1] in vowels:
                pre_count -= 1
            if s[j] in vowels:
                pre_count += 1
            if _max < pre_count:
                _max = pre_count
        return _max




if __name__ == '__main__':
    assert Solution().maxVowels("abciiidef", 3) == 3
    assert Solution().maxVowels("aeiou", 2) == 2
    assert Solution().maxVowels("weallloveyou", 7) == 4
    assert Solution().maxVowels("tryhard", 4) == 1
