"""
mplement atoi to convert a string to an integer.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
            flag = 1
        else:
            flag = 1
        res = 0
        for i in range(len(str)):
            if not str[i].isalnum():
                return flag * res
            try:
                res = res * 10 + int(str[i])
            except:
                return flag * res 
            if res * flag > 2147483647:
                return 2147483647
            elif res * flag < -2147483648:
                return -2147483648
        return flag * res
