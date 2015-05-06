/*
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL && l2 == NULL)
            return NULL;
        else if (l1 == NULL)
            return l2;
        else if (l2 == NULL)
            return l1;

        ListNode* tmp = NULL;
        if (l1->val > l2->val) {
            tmp = l2;
            tmp->next = mergeTwoLists(l1, tmp->next);
        } 
        else {
            tmp = l1;
            tmp->next = mergeTwoLists(l2, tmp->next);
        }
        return tmp;
    }
};
