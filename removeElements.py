"""

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None or val is None:
            return head


        pre = None
        p = head

        while p is not None:
            if p.val == val:
                if pre is None:
                    pre = None
                    head = head.next
                else:
                    pre.next = p.next
            else:
                pre = p
            p = p.next
        return head



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)
#node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

def printNode(node):
    p = node
    while p is not None:
        print p.val
        p = p.next

printNode(node1)



s = Solution()
node = s.removeElements(node1, 1)

printNode(node)
