/*
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.


Analysis:
1.find the mid node, then split in two list
2.reverse the seconde list
3.merge two list
*/

#include <iostream>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return;
        ListNode* p = head;
        ListNode* mid = findMid(head);

        ListNode* tmp = mid->next;
        mid->next = NULL;
       
        ListNode* q = tmp->next; 
        tmp->next = NULL;
        while (q != NULL) {
            ListNode* next = q->next;
            q->next = tmp;
            tmp = q;
            q = next;
        } 

        while (tmp != NULL) {
           q = tmp->next;
           tmp->next = p->next;
           p->next = tmp;
           tmp = q;
           p = p->next->next;
        } 

    }
    
    ListNode* findMid(ListNode* head) {
        ListNode* mid = head;
        ListNode* last = head->next;
        while(last && last->next) {
            mid = mid->next;
            last = last->next->next;
        }
        return mid;
    }
};

int main(int argc, char** argv)
{
    ListNode* l1 = new ListNode(1);    
    ListNode* l2 = new ListNode(2);    
    l1->next = l2;
    ListNode* l3 = new ListNode(3);    
    l2->next = l3;
    ListNode* l4 = new ListNode(4);    
    l3->next = l4;

    Solution a;
    a.reorderList(l1);

    while(l1 != NULL) {
        cout<<l1->val<<">";
        l1 = l1->next;
    }
    
    return 0;
}
