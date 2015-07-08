class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        tmp = s.strip()
        l = 0
        for i in range(len(tmp)):
            if tmp[i] == " ":
                l = 0
            else:
                l += 1
        return l
