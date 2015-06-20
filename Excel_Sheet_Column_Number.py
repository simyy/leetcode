class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        d = {}
        for i in range(26):
            d[(chr(ord('A') + i))] = i + 1
          
        res = 0
        for i in range(len(s)):
            if i == 0:
                res += d[s[len(s) - i - 1]]
            else:
                res += (26**i) * d[s[len(s) - i - 1]]
        return res
