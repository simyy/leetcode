/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
*/

#include <iostream>

using namespace std;


struct IntStack{
    int data;
    IntStack* min;
    IntStack* pre;
};


class MinStack {
public:
    MinStack(){
        tail = NULL;
    }
    ~MinStack(){
    }
    void push(int x) {
       IntStack* p = new IntStack;
       p->data = x;
       if (tail == NULL){
           tail = p;
           tail->min = tail;
           p->pre  = NULL;
       }
       else{
           if (x > tail->min->data)
               p->min = tail->min;
           else 
               p->min = p;
           p->pre = tail;
           tail = p;
           
       }
    }

    void pop() {
        if (tail == NULL){
            IntStack* p = tail;
            tail = tail->pre;
            delete p;
        }
    }

    int top() {
        if (tail == NULL)
            return 0;
        return tail->data;
    }

    int getMin() {
        if (tail == NULL)
            return 0; 
        return tail->min->data;
    }
private:
    IntStack* tail;
};

int main()
{
    MinStack s;
    for(int i=0; i<100; i++){
        s.push(-2);
        s.push(0);
        s.push(-1);
        cout<<s.getMin()<<endl;
        cout<<s.top()<<endl;
        s.pop();
        cout<<s.getMin()<<endl;

        s.push(2147483647);
        cout<<s.top()<<endl;
        cout<<s.getMin()<<endl;
        s.push(-2147483648);
        cout<<s.top()<<endl;
        cout<<s.getMin()<<endl;
        s.pop();
        cout<<s.getMin()<<endl;
    }
    return 0;
}
