# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return None
        p = head
        q = head.next
        while q != None:
            if p.val == q.val:
                p.next = q.next
                q = p.next
            else:
                p = p.next
                q = p.next
        return head
            
