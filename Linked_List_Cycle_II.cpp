/*
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Analysis:
when two pointer came to common ponit, the length of the fast pointer must be double length of the show pointer. 
*/

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* p = head;
        ListNode* q = head;
        while (p && p->next) {
            p = p->next->next;
            q = q->next;
            if (p == q) {
                p = head;
                while (p != q) {
                    p = p->next;
                    q = q->next;
                }
                return q;
            }
        }
        return NULL;
    }
};
