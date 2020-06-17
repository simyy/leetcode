# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

先把节点层级调整一致，然后在同步向上调整找到公共节点
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        memo = {}

        def dfs(node, sub_root, deep=0):
            if sub_root is None:
                return -1
            if sub_root.val == node.val:
                return deep
            if sub_root.left:
                memo[sub_root.left.val] = sub_root
            l_rs = dfs(node, sub_root.left, deep + 1)
            if l_rs != -1:
                return l_rs
            if sub_root.right:
                memo[sub_root.right.val] = sub_root
            r_rs = dfs(node, sub_root.right, deep + 1)
            if r_rs != -1:
                return r_rs
            return -1

        deep_of_p = dfs(p, root)
        deep_of_q = dfs(q, root)

        if deep_of_p > deep_of_q:
            i = 0
            while i < deep_of_p - deep_of_q:
                p = memo[p.val]
                i += 1
        elif deep_of_p < deep_of_q:
            i = 0
            while i < deep_of_q - deep_of_p:
                q = memo[q.val]
                i += 1

        while True:
            if p.val == q.val:
                return p
            else:
                p = memo[p.val]
                q = memo[q.val]
        return None




if __name__ == '__main__':
    a0 = TreeNode(0)
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)
    a6 = TreeNode(6)
    a7 = TreeNode(7)
    a8 = TreeNode(8)

    root = a3
    a3.left = a5
    a3.right = a1
    a5.left = a6
    a5.right = a2
    a2.left = a7
    a2.right = a4

    a1.left = a0
    a1.right = a8

    print Solution().lowestCommonAncestor(root, a5, a1).val
    print Solution().lowestCommonAncestor(root, a5, a4).val