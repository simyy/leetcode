# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        i = 0
        while i < len(S) and S[i] != '-':
            i += 1
        root = TreeNode(S[:i])
        deep_parent = [root]
        # i = 1
        pre_deep = 0
        while i < len(S):
            deep = 0
            while i < len(S) and S[i] == '-':
                deep += 1
                i += 1
            s = i
            while i < len(S) and S[i] != '-':
                i += 1
            num = int(S[s:i])

            node = TreeNode(num)
            if deep > pre_deep:
                deep_parent[-1].left = node
                deep_parent.append(node)
                pre_deep = deep
            elif deep == pre_deep:
                deep_parent[-2].right = node
                deep_parent.pop(-1)
                deep_parent.append(node)
            else:
                back = pre_deep - deep
                while back >= 0:
                    deep_parent.pop(-1)
                    back -= 1
                deep_parent[-1].right = node
                deep_parent.append(node)
                pre_deep = deep

        return root

    def recoverFromPreorder1(self, S):
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]







if __name__ == '__main__':
    # print Solution().recoverFromPreorder("1-2--3--4-5--6--7")
    # print Solution().recoverFromPreorder("1-2--3---4-5--6---7")
    # print Solution().recoverFromPreorder("1-401--349---90--88")
    # root = Solution().recoverFromPreorder("1-401--349--90---88")
    # root1 = Solution().recoverFromPreorder1("1-401--349--90---88")
    print Solution().recoverFromPreorder("10-7--8")