"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.toNum(l1)
        n2 = self.toNum(l2)
        n = n1 + n2
        return self.toList(n)

    def toNum(self, l):
        r = 0
        p = l
        i = 0
        while p:
            r += p.val * 10 ** i
            p = p.next
            i += 1
        return r

    def toList(self, n):
        h = None
        p = None
        if n == 0:
            return ListNode(0)
        while n != 0:
            x = n % 10
            n = n / 10
            q = ListNode(x)
            if not h:
                h = q
                p = q
                continue
            p.next = q
            p = q
        return h
        
