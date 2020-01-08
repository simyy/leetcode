# -*- coding: utf-8 -*-

# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[in
        """
        rs = []
        self.recursion(root, rs)
        return rs

    def recursion(self, root, rs):
        if not root:
            return
        if root.left:
            self.recursion(root.left, rs)
        rs.append(root.val)
        if root.right:
            self.recursion(root.right, rs)

if __name__ == '__main__':

    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)

    root.right = n1
    n1.left = n2

    s = Solution()
    print s.inorderTraversal(root)
