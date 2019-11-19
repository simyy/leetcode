"""
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

Analysis：

Method:

1> merge sort, loop every list
2> heap sort, build a min list
3> magic, build a sort array, then get a node list

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    Time Limit Exceeded
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        p = None
        j = None
        for i in range(len(lists)):
            if not lists[i]:
                continue
            if not p or p.val > lists[i].val:
                p = lists[i]
                j = i
        if not p:
            return None
        lists[j] = lists[j].next
        p.next = self.mergeKLists(lists)
        return p

    def mergeKLists_use_list(self, lists):
        array = []
        for head in lists:
            while head is not None:
                array.append(head.val)
                head = head.next
        array.sort()
        head = None
        prev = None
        for val in array:
            node = ListNode(val)
            if head is None:
                head = node
            if prev is not None:
                prev.next = node
            prev = node
        return head






n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(5)
n1.next = n2
n2.next = n3

n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n4.next = n5
n5.next = n6

n7 = ListNode(2)
n8 = ListNode(6)
n7.next = n8

s = Solution()
node = s.mergeKLists_use_list([n1, n4, n7])

p = node
while p:
    print p.val
    p = p.next
