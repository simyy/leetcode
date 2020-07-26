# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/contest/weekly-contest-199/problems/number-of-good-leaf-nodes-pairs/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        self.rs = []
        self.dfs(root, distance)
        return len(self.rs)

    def dfs(self, root, distance):
        if not root:
            return None
        if root.left is None and root.right is None:
            return [[root.val, 1]]
        left_leaf = self.dfs(root.left, distance)
        right_leaf = self.dfs(root.right, distance)
        # 过滤超长的
        if left_leaf:
            left_leaf = filter(lambda x: x[1] < distance, left_leaf)
        if right_leaf:
            right_leaf = filter(lambda x: x[1] < distance, right_leaf)
        if left_leaf and right_leaf:
            # 计算distance
            for a in left_leaf:
                for b in right_leaf:
                    if a[1] + b[1] <= distance:
                        self.rs.append([a[0], b[0]])
                        # 为什么不需要判断重复？ 是由于只会左右子树判断，不会存在重复情况
                        # if [a[0], b[0]] not in self.rs:
                        #     self.rs.append([a[0], b[0]])
        leaf = []
        if left_leaf:
            leaf += [[leaf[0], leaf[1]+1] for leaf in left_leaf]
        if right_leaf:
            leaf += [[leaf[0], leaf[1]+1] for leaf in right_leaf]
        return leaf


if __name__ == '__main__':

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2.left = n4
    n2.right = n5
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n3.left = n6
    n3.right = n7

    assert Solution().countPairs(n1, 3) == 2