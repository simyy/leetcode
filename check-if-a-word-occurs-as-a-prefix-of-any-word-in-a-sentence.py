# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
"""

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        space = 0
        i = 0
        while i < len(sentence):
            if sentence[i] == ' ':
                space += 1
            if i == 0 or sentence[i - 1] == ' ':
                match = True
                j = i
                while j < len(sentence) and j < i + len(searchWord):
                    if sentence[j] != searchWord[j - i]:
                        match = False
                    j += 1
                if match:
                    return space + 1
            i += 1
        return -1


if __name__ == '__main__':
    assert Solution().isPrefixOfWord("i love eating burger", "burg") == 4
    assert Solution().isPrefixOfWord("this problem is an easy problem", "pro") == 2
    assert Solution().isPrefixOfWord("hello from the other side", "they") == -1
    assert Solution().isPrefixOfWord("hellohello hellohellohello", "ell") == -1
