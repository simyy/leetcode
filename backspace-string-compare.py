# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors. \
# means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?


Analysis:
1. '#' means backspace, then compare from right.
2. Find the first char in sub-string, which had no backspace char '#' at the end.
3. Compare substring in S and T, until S[i] != S[j] or (i < 0 or j < 0).
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # Compare string from right to left
        i = len(S) - 1
        j = len(T) - 1
        while i >= 0 or j >= 0:
            back_s = 0

            # Get the first char in sub string in reverse order
            while i >= 0:
                # If case '#', then backspace
                if S[i] == '#':
                    back_s += 1
                    i -= 1
                else:
                    # If backspace > 0, then move left, else break (case a char)
                    if back_s > 0:
                        i -= 1
                        back_s -= 1
                    else:
                        break

            # The same logic for string T
            back_t = 0
            while j >= 0:
                if T[j] == '#':
                    back_t += 1
                    j -= 1
                else:
                    if back_t > 0:
                        j -= 1
                        back_t -= 1
                    else:
                        break

            # If exist one char in S or T, then compare S[i] and T[j]
            if i >= 0 and j >= 0:
                # Equal char, then i and j move left, otherwise not equal, break
                if S[i] == T[j]:
                    i -= 1
                    j -= 1
                else:
                    break
            else:
                break

        # After compare every char, i and j must be -1
        if i == j == -1:
            return True
        return False


if __name__ == '__main__':
    print Solution().backspaceCompare("ab#c", "ad#c")
    print Solution().backspaceCompare("ab##", "c#d#")
    print Solution().backspaceCompare("a##c", "#a#c")
    print Solution().backspaceCompare("a#c", "b")
    print Solution().backspaceCompare("bxj##tw", "bxj###tw")
    print Solution().backspaceCompare("bbbextm", "bbb#extm")
    print Solution().backspaceCompare("nzp#o#g", "b#nzp#o#g")
