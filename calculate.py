# -*- coding: utf-8 -*-

"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
    The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Analysis:
Priority calculate '*' and '/'，then recalculate with number, '+' and '-'.

1. Skip whitespace;
2. Combine number until reach operator, marked PreNumber
3. Use a stack record number, '+' and '-';
4. Use priorityOperator record '*' or '/';
5. If priorityOperator is not None, direct calculate preNum with prePreNum(last in stack)
    recalculate preNum by lastStackNumber * preNum
    clear priorityOperator to None
6. If reach an operator,
     push preNum to stack
     clear preNum to 0
     if operator is priorityOperator:
        marked operator as priorityOperator

Step 5 is KEY!!!

"""

class Solution:
    def calculate(self, s):
        # empty string, return 0
        if not s:
            return 0
        # User a stack
        stack = []
        # Record pre number
        preNum = 0
        # Record current operator
        priorityOperator = None
        # traverse string
        for i in xrange(len(s)):
            # build number, then continue
            if s[i].isdigit():
                preNum = preNum * 10 + ord(s[i]) - ord('0')
                if i < len(s) - 1:
                    continue
            # skip whitespace, then continue
            if s[i].isspace() and i < len(s) - 1:
                continue

            if priorityOperator is not None:
                if priorityOperator == '*':
                    preNum = stack.pop() * preNum
                else:
                    preNum = stack.pop() / preNum
                priorityOperator = None

            # Push preNum to stack
            stack.append(preNum)
            # Clear preNum
            preNum = 0

            char = s[i]
            if char in ['+', '-']:
                stack.append(char)
            else:
                priorityOperator = char

        if preNum > 0:
            stack.append(preNum)

        for i in range(len(stack)):
            if stack[i] == '+':
                stack[i] = 0
            elif stack[i] == '-' and i < len(stack) - 1:
                stack[i] = 0
                stack[i + 1] = - stack[i + 1];
            else:
                stack[i] = int(stack[i])
        return sum(stack)

if __name__ == '__main__':
    # print Solution().calculate("3+2*2")
    # print Solution().calculate(" 3/2 ")
    # print Solution().calculate(" 3+5 / 2 ")
    # print Solution().calculate("0-2147483647")
    print Solution().calculate("2*3+4")
