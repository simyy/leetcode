"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
"""

#!/usr/bin/env python
# encoding:utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        self.invert(root)
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root

    def invert(self, node):
        tmp = node.left
        node.left = node.right
        node.right = tmp


if __name__ == "__main__":
    a = Solution()
    b1 = TreeNode(2)
    b1.left = TreeNode(1)
    b1.right = TreeNode(3)
    b2 = TreeNode(7)
    b2.left = TreeNode(6)
    b2.right = TreeNode(9)
    root = TreeNode(4)
    root.left = b1 
    root.right = b2 
    res = a.invertTree(root)
    l = [res] 
    while len(l) > 0:
        n = len(l)
        for i in range(n):
            print l[i].val
            if l[i].left:
                l.append(l[i].left)
            if l[i].right:
                l.append(l[i].right)
        print "######"
        l = l[n:]
