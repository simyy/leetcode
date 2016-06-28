"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Analysis:
1. 每次计算都与前两个数的取值有关
2. 确定前两个值之后就可以使用递归
3. 递归的边界条件是刚好相等且递归结束（没有数据了）

"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i = 0
        for j in range(1, len(num) - 1):
            for k in range(j + 1, len(num)):
                if self.valid(num, i, j, k):
                    return True
        return False

    def valid(self, num, i, j, k):
        if (j - i != 1 and num[i] == '0') \
            or (k - j != 1 and num[j] == '0'):
            return False
        first = int(num[i:j])
        second = int(num[j:k])
        for x in range(k + 1, len(num) + 1):
            if x - k != 0 and num[k] == '0':
                continue
            new = int(num[k:x])
            if first + second > new:
                continue
            elif first + second < new:
                return False
            else:
                if x == len(num):
                    return True
                return self.valid(num, j, k, x)
        return False
