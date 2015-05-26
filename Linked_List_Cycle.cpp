/*
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?

Analysis:
a cycle must be tail->next=head,  we can get pointer p move to next step, and move pointer q to next two step, 
then no matter how much it must be have a time get a common place.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* p = head;
        ListNode* q = head;
        while (p && p->next) {
            p = p->next->next;
            q = q->next;
            if (p == q)
                return true;
        }
        return false;
    }
};
