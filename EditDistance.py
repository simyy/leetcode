"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

Analysis:
DP solution.
1. if word1 or word2 is zero, then stop, return max length;
2. make a matrix which means distance between word[:i] and word[:j] 
   the matrix_i_0 is i where i in len(word1) + 1, and the matrix_0_j is j where j in len(word2) + 1
3. after init matrix, then cmp word[i] and word[j] where i < len(word1) + 1 and j < len(word2)+ 1，
   if word[i] == word[j], then dis between word[:i] and word[:j] must equal matrix[i-1][j-1]
   else dis equal min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
4. matrix[i][j] is result
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        if len1 == 1 or len2 == 1:
            return max(len1, len2) - 1
        dis = [[0 for j in range(len2)] for i in range(len1)]
        for i in range(len1):
            dis[i][0] = i
        for j in range(len2):
            dis[0][j] = j

        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i - 1] == word2[j - 1]:
                    dis[i][j] = dis[i - 1][j - 1]
                else:
                    dis[i][j] = min(dis[i - 1][j - 1], dis[i-1][j], dis[i][j-1]) + 1
        return dis[i][j]
