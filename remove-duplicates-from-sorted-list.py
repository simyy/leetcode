# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/delete-node-in-a-linked-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

Analysis:
1. Background: sorted list.
2. To remove node, it need two pointer to record pre and current node.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def buildList(cls, nums):
        if not nums:
            return None
        head = None
        pre = None
        for num in nums:
            node = ListNode(num)
            if not head:
                head = node
            if pre:
                pre.next = node
            pre = node
        return head

    @classmethod
    def printList(cls, head):
        nums = []
        p = head
        while p:
            nums.append(str(p.val))
            p = p.next
        print "->".join(nums)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        # Use two pointer, p is first and q is second
        p = head
        q = head.next
        while q != None:
            # If duplicate, then remove q
            if p.val == q.val:
                p.next = q.next
                q = p.next
            else:
                p = p.next
                q = p.next
        return head


if __name__ == '__main__':

    head = ListNode.buildList([1, 1, 2])
    ListNode.printList(head)

    s = Solution()
    s.deleteDuplicates(head)
    ListNode.printList(head)
