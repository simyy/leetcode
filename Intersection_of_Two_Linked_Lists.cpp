/*
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Analysis:
这个题目是为了找到两个链表的相交点，而且题目中已经假设不存在环，那么也就是说交点只有一个，交点到链表尾部应该是相同的。

因此，对于上面的例子来说，我们只需要比较长度相等的一段，那么，由于B比A长，我们只需要比较a1->c3与b2->c3这段相等长度的链表。

*/

#include<iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(!headA || !headB)
            return NULL;            
        
        int lenA = 0;
        ListNode *pa = headA;
        while(pa){
            lenA++;
            pa = pa->next;
        }

        int lenB = 0;
        ListNode *pb = headB;
        while(pb){
            lenB++;
            pb = pb->next;
        }
        /* get the diffrent element size */
        int lenDiff = lenA - lenB;
        pa = headA;
        pb = headB;

        /* get the font of the compare list */
        if(lenDiff > 0) {
            while(lenDiff != 0) {
                pa = pa->next;
                lenDiff--;
            }
        }
        else if(lenDiff < 0) {
            while(lenDiff != 0) {
                pb = pb->next;
                lenDiff++;
            }
        }

        while(pa&&pb) {
            if(pa == pb)
                return pa;
            pa = pa->next;
            pb = pb->next;
        }

        return NULL;
    }
};

int main(int argc, char** argv)
{
    ListNode* headA = new ListNode(1);
    ListNode* A1 = new ListNode(2);
    headA->next = A1;

    ListNode* headB = new ListNode(1);
   
    ListNode* x = new ListNode(3); 
    A1->next = x;
    headB->next = x;

    int i = 5;
    while(i > 0){
        ListNode* Ax = new ListNode(i);
        x->next = Ax;
        x = Ax;
        i--;
    }

    Solution *a;
    ListNode* res = a->getIntersectionNode(headA, headB);
    if (res == NULL)
       cout<<"NULL"<<endl; 
    else
        cout<<res->val<<endl;

    return 0;
}
