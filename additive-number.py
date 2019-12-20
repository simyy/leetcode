# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/additive-number/

Additive number is a string whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Analysis:
#1. 每次计算都与前两个数的取值有关
#2. 确定前两个值之后就可以使用递归
#3. 递归的边界条件是刚好相等且递归结束（没有数据了）



"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # Use i/j/k marked two numbers
        # num[i:j] and nums[j:k]
        # Where i < j < k
        i = 0
        for j in range(1, len(num) - 1):
            for k in range(j + 1, len(num)):
                # Traverse every i/j/k
                if self.valid(num, i, j, k):
                    return True
        return False

    def valid(self, num, i, j, k):
        """
        num[i:j] + nums[j:k] ? nums[k:x], x is unknown
        """
        # Invalid, num[i:j] or nums[j:k stars with zero
        if (j - i != 1 and num[i] == '0') \
            or (k - j != 1 and num[j] == '0'):
            return False
        # Get first and second number
        first = int(num[i:j])
        second = int(num[j:k])
        # find the x to meet num[i:j] + nums[j:k] == nums[k:x]
        for x in range(k + 1, len(num) + 1):
            #  # Invalid, nums[k:x] stars with zero
            if x - k != 1 and num[k] == '0':
                continue
            third = int(num[k:x])
            # Less than, k move to right
            if first + second > third:
                continue
            # More than, return False (right is more than current)
            elif first + second < third:
                return False
            # Equal
            else:
                # If nums[j:x] is last sub string, return True
                if x == len(num):
                    return True
                # recursion  j/k/x
                return self.valid(num, j, k, x)
        return False


if __name__ == '__main__':
    print Solution().isAdditiveNumber("112358");
    print Solution().isAdditiveNumber("199100199");
    print Solution().isAdditiveNumber("000");
