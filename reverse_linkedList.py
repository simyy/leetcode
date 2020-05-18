# -*- coding: utf-8 -*-

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list(head):
    r_head = None
    p = head
    while p:
        q = p.next
        p.next = r_head
        r_head = p
        p = q
    return r_head


def print_linked_list(head):
    p = head
    r = []
    while p:
        if p.val:
            r.append(p.val)
        p = p.next
    print '->'.join([str(_) for _ in r])


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    print_linked_list(head)
    print_linked_list(reverse_linked_list(head))
