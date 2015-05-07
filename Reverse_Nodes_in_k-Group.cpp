/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Analysis:
同上一题，同样考察链表的问题，其实这里外加考察了堆栈先进后出的原理；
同样这里需要注意prev指针和next指针的变化以及head指针的变化；
利用堆栈实现链表的倒置；
*/



#include <iostream>
#include <stack>
using namespace std;

struct ListNode {
   int val;
   ListNode *next;
   ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == NULL)
            return head;
        stack<ListNode*> reverse;
        ListNode* prev = NULL;
        initReverse(reverse, prev, k, head);

        if (reverse.size() < k)
            return head;

        head = reverse.top();

        while(reverse.size() == k) {
            reverseGroup(reverse, prev);
            initReverse(reverse, prev, k, head);
        }
        return head;
    }

    void initReverse(stack<ListNode*>& reverse, ListNode* prev, int k, ListNode* head)
    {
        ListNode* p = NULL;
        if (prev == NULL)
            p = head; 
        else
            p = prev->next;
        while (k-- > 0 && p != NULL) {
            reverse.push(p);
            //cout<<"push :"<<p->val<<endl;
            p = p->next;
        }
    }

    void reverseGroup(stack<ListNode*>& reverse, ListNode* &prev)
    {
        int len = reverse.size();
        ListNode* next = reverse.top()->next;
        //cout<<"next :"<<next->val<<endl;
        if (prev == NULL) {
            //cout<<"prev :"<<reverse.top()->val<<endl;
            prev = reverse.top();
            reverse.pop();
        }
        while(!reverse.empty()) {
            prev->next = reverse.top();
            reverse.pop();
            prev = prev->next;
        }
        prev->next = next;
        //cout<<"prev->next :"<<next->val<<endl;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    ListNode* x = new ListNode(1);
    ListNode* y = new ListNode(2);
    ListNode* z = new ListNode(3);
    ListNode* h = new ListNode(4);
    ListNode* k = new ListNode(5);
    x->next = y;
    y->next = z;
    z->next = h;
    h->next = k;

    ListNode* head = a.reverseKGroup(x, 1);
    ListNode* p = head;
    while (p != NULL) {
        cout<<p->val<<" ";
        p = p->next;
    }
    cout<<endl;

    return 0;
}
