"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

"""

class Solution(object):
    """
    Result: Time Limit Exceeded 
    """
    def reverseVowels(self, s):
        r = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vowel_index = []
        for i in range(len(s)):
            r.append(s[i])
            if s[i] in vowels:
                vowel_index.append(i)
                for j in range(len(vowel_index) - 1, 0, -1):
                    r[vowel_index[j]], r[vowel_index[j - 1]] = \
                        r[vowel_index[j - 1]], r[vowel_index[j]]
        return ''.join(r)
