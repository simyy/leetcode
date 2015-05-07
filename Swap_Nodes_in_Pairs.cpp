/*
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Analysis:
此题考查链表的遍历问题，由于考虑到数据是一对一对交换的，那么需要指定2个指针。
由于本体中的ListNode的单向链表，因此不能连接前后连段元素，这样增加1个指针，如下：
两个指针的情况（q,p）： s->p->q->r，有p->next=q->next, q->next=p，但是s->next依然等于p
三个指针的情况（s,q,p）：s->p->q->r，有p->next=q->next, q->next=p，s->next=q
需要注意：在第一做交换的时候，head的头指针发生了变化，指向了第二个元素，需要改变head指针。
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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL)
          return head;
        ListNode* p = head;
        ListNode* q = head->next;
        ListNode* prev = NULL;

        while(q != NULL) {
            p->next = q->next;
            q->next = p;
            if (prev != NULL)
                prev->next = q;
            else
                head = q;
            prev = p;
            p = p->next;
            if (p != NULL)
                q = p->next;
            else
                break;
        }
        return head;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    ListNode* x = new ListNode(1);
    ListNode* y = new ListNode(2);
    ListNode* z = new ListNode(3);
    ListNode* h = new ListNode(4);
    x->next = y;
    y->next = z;
    z->next = h;

    ListNode* head = a.swapPairs(x);
    ListNode* p = head;
    while (p != NULL) {
        cout<<p->val<<" ";
        p = p->next;
    }
    cout<<endl;

    return 0;
}
