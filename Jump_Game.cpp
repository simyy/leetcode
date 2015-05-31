/*
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

Analysis:
the second condition is very import, the muximum jump means it can select a length less then it,
so we can get the longest length between nums[i] and last longest one,
if the max one is less then 0, it must be false.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() <= 1)
            return true;
        int length = nums[0];
        if (length <= 0 && nums.size() > 1)
            return false;
        for (int i = 1; i < nums.size()-1; ++i) {
            length = max(length - 1, nums[i]);
            cout<<"length:\t"<<length<<endl;
            if (length <= 0) 
                return false;
        }
        return true;
    }
};


int main(int argc, char** argv)
{
    int a[] = {1, 0, 2};
    vector<int> nums (a, a + sizeof(a) / sizeof(int));
    Solution b;
    bool result = b.canJump(nums);
    if (result)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl; 
    return 0;
}
