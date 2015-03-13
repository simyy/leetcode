/*
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Analysis:
  问题是为了找到一个数组中出现的重复次数大于一半的数字。
  如果一个数字出现的次数超过一半（可以这样表示(n+m)/2n > 1/2：n＊重复+n＊其他+m*重复），那么可以利用消除的方法，就是利用一个重复数字消除一个其他数字，剩下的必然是重复数字。
  可以分为三步：
  1.首先取第一个数字为major，那么count为1。
  2.取下一个数字，如果相同,count=count+1，否则，消除,count=count-1。
  3.当count为0时，重复1。
  4.当count > n/2时，即可停止。
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int> &num) {
        int major = num[0];
        int count = 1;
        for (int i = 1; i < num.size(); i++) {
            if (count > num.size()/2) {
                return major;
            }
            if (count == 0) {
                count = 1;
                major = num[i];
            }
            else if (major == num[i]) {
                count++;
            }
            else
                count--;
        }

        return major;
    }
};

int main()
{
    vector<int> a;
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    a.push_back(4);
    a.push_back(5);
    a.push_back(1);
    a.push_back(1);
    a.push_back(1);
    a.push_back(1);
    a.push_back(1);

    Solution xx;
    int r = xx.majorityElement(a);
    
    cout<<r<<endl;

    return 0;
}
