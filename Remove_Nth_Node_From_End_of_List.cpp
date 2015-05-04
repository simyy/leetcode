/*
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
   
Analysis:
此题主要是链表的遍历问题，由于需要遍历一次找到倒序中某个元素，那么采用一个指针是不够的，因此
1.采用两个指针分别指向first=head和second=head+n
2.两个指针同时向后移动，只要second达到链表尾部，那么first必然停留在倒数第n个元素位置（由于first和second之间相差n个元素）
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p = head;
        ListNode* q = head;
        ListNode* pre = head;
        while (p != NULL) {
            if (n > 0) 
                n--;
            else {
                pre = q;
                q = q->next;
            }
                
            p = p->next;
        }

        if (q == head) {
            head = head->next;
            delete p;
        }
        else {
            pre->next = q->next;
            delete q;
        }

        return head;
    }
};

int main(int argc, char** argv)
{
    Solution a;
    int i = 1;
    ListNode* p = new ListNode(i++);
    ListNode* head = p;
    while(i <= 5) {
        ListNode* q = new ListNode(i++);
        p->next = q;
        p = q;
    }
    p = a.removeNthFromEnd(head, 2);

    cout<<p->val;
    p = p->next;
    while( p != NULL) {
        cout<<"->"<<p->val;
        p = p->next;
    }
    cout<<endl;

    return 0;
}
