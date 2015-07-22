"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        return self.eq(p, q)
    
    def eq(self, node1, node2):
        if node1 == None or node2 == None:
            if node1 == node2:
                return True
            else:
                return False
        elif node1.val == node2.val:
            return self.eq(node1.left, node2.left) and self.eq(node1.right, node2.right)
        else:
            return False
