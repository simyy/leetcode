# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-common-subsequence/
"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        rows = len(text1) + 1
        columns = len(text2) + 1
        dp = [[0 for _ in range(columns)] for __ in range(rows)]

        for i in range(1, rows):
            for j in range(1, columns):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    # assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    # assert Solution().longestCommonSubsequence("abc", "abc") == 3
    # assert Solution().longestCommonSubsequence("abc", "def") == 0
    assert Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == 4