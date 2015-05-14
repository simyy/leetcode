/*
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

Analysis:
二分法
*/

#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0)
            return 0;
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r) {
            if (nums[l] >= target)
                return l;
            else if (nums[r] == target)
                return r;
            else if (nums[r] < target)
                return r + 1;
            int mid = (l + r) / 2;
            if (nums[mid] > target)
                r = mid - 1;
            else if (nums[mid] < target)
                l = mid + 1;
            else
                return mid;

        }
        return l;
    }
};

int main(int argc, char** argv)
{
    Solution a;
    vector<int> nums;
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(5);
    nums.push_back(6);
    int res = a.searchInsert(nums, 5);
    cout<<res<<endl;

    return 0;
}
