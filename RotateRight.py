"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Analysis:
User fist and second pointer, which distance is k % length, then move two pointer, change fist and second next node.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
    
        first, second = head, head
        l = 0
        while second:
            l += 1
            second = second.next
    
        second = head
        for i in range(k%l):
            second = second.next
    
        while second.next:
            second = second.next
            first = first.next
    
        second.next = head
        head = first.next
        first.next = None
    
        return head
            
