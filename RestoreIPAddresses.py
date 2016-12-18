"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution:
    def restoreIpAddresses(self, s):
        result = []
        self.restore(s, 0, 0, "", result)
        return result

    def restore(self, s, index, count, ip, result):
        if count == 4:
            if index == len(s):
                result.append(ip)
            return

        last = index + 3 if index + 3 <= len(s) else len(s)
        for i in range(index, last):
            tmp = int(s[index:i+1])
            if tmp > 255:
                break

            if s[index] == "0" and i != index:
                continue

            tmp_ip = ip + s[index:i+1]
            print s[index:i+1]
            print ip , "=>", tmp_ip
            if count <= 2:
                tmp_ip += "."

            self.restore(s, i + 1, count + 1, tmp_ip, result)

print Solution().restoreIpAddresses("25525511135")
print Solution().restoreIpAddresses("010010")
