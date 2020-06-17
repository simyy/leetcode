# -*- coding: utf-8 -*-

"""
LCA

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

二叉搜索树是有序的，左子树小于右子树
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
        if root is None:
            return None
        a, b = p.val, q.val
        if p.val > q.val:
            a, b = q.val, p.val
        if a <= root.val <= b:
            return root
        elif a < root.val and b < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    root = TreeNode(6)
    a2 = TreeNode(2)
    a8 = TreeNode(8)
    a0 = TreeNode(0)
    a4 = TreeNode(4)
    a7 = TreeNode(7)
    a9 = TreeNode(9)
    a3 = TreeNode(3)
    a5 = TreeNode(5)
    root.left = a2
    root.right = a8
    a2.left = a0
    a2.right = a4
    a4.left = a3
    a3.left = a5
    a8.left = a7
    a8.right = a9

    print Solution().lowestCommonAncestor(root, a2, a8)


