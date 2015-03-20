/*
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    
Analysis:
  本题目类似于10进制转16进制一样，可以利用求余的方法倒序转换，转化为26进制。需要注意：在这里没有0的概念，
  那么26是Z，而27=1+1*26，则27为AA，那么52呢？52=0+2*26,但由于没有0，则变为52=26+1＊26,为AZ
    
  */


#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    string convertToTitle(int n) {
        string res("");
        stack<char> s;
        while (n > 0) {
            if (n%26 == 0) {
                if (n/26 > 1){
                    s.push('Z');
                    n -= 1;
                }
                else if (n/26 == 1){
                    s.push('Z');
                    n = n/26;
                }
            }
            else
                s.push('A' + n%26 - 1);
            cout<<s.top()<<endl;
            n = n/26;
        }
        while(!s.empty()) {
            res.push_back(s.top());
            s.pop();
        }
        return res; 
    }
};

int main(int argc, char** argv) 
{
    Solution a;

    int x;
    cin>>x;
    string aa = a.convertToTitle(x);
    cout<<aa<<endl;

    cout<<(char)('A'+25)<<endl;

    return 0;
}
