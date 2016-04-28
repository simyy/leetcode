"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Analysis:
1. record all vowels in string;
2. revserse the record vowel list;
3. make a new groups again by reverse vowel list.
"""

class Solution(object):
    """
    Result: Time Limit Exceeded
    Reason: use a bubble sort method to move vowels, slow!!!!! 
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
        
        
class Solution(object):
    """
    Result: Accept
    """
    def reverseVowels(self, s):
        r = []
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowel_index = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_index.append(i)
        last = len(vowel_index) - 1
        for i in range(len(s)):
            if s[i] in vowels:
                r.append(s[vowel_index[last]])
                last -= 1
            else:
                r.append(s[i])
        return ''.join(r)
