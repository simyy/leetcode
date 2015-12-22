"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Analysis:
1. use a stack to store all the all number, and op record last operator
2. it is simply that not contains '(' or ')'， then just calculate in order
3. jump of space 
"""

class Solution:
    def calculate(self, s):
        if not s:
            return 0

        prev  = 0
        op    = ''
        stack = []

        for i in xrange(len(s)):
            if s[i].isdigit():
                prev = prev * 10 + ord(s[i]) - ord('0')
                if i < len(s) - 1:
                    continue

            if s[i].isspace() and i < len(s) - 1:
                continue
            
            if op == '':
                stack.append(prev)
            elif op == '+':
                stack.append(prev)
            elif op == '-':
                stack.append(-prev)
            elif op == '*':
                tmp = stack.pop()
                stack.append(tmp * prev)
            else:
                tmp = stack.pop()
                if tmp < 0:
                    stack.append(-(-tmp/prev))
                else:
                    stack.append(tmp / prev)


            op = s[i]
            prev = 0

        return sum(stack)
