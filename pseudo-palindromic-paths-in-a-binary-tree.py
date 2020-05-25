# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rs = 0
        self.dfs(root, [])
        return self.rs

    def judge(self, path):
        d = []
        for node in path:
            if node not in d:
                d.append(node)
            else:
                d.remove(node)
        if len(d) == 0 or len(d) == 1:
            self.rs += 1

    def dfs(self, root, path):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            self.judge(path)
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)
        path.pop(-1)


if __name__ == '__main__':

    assert Solution().pseudoPalindromicPaths([2,3,1,3,1,None,1]) == 2
    assert Solution().pseudoPalindromicPaths([2,1,1,1,3,None,None,None,None,None,1]) == 1
    assert Solution().pseudoPalindromicPaths([9]) == 1