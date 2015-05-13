/*
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Analysis:
有序数组经过旋转，仍然会变为一个有序的数组，例如
0 1 2 4 5 6 7 -> 4 5 6 7 0 1 2-> 7 0 1 2 4 5 6 -> 1 2 4 5 6 7 0
可以看出规律：无论转换多少次，其实都是可以经过一次旋转得到，因此，会有两种情况：1个递增序列和2个递增序列（前一个均大于后一个）。
利用二分法求解即可，复杂度为o(logn)
1.mid=(left+right)/2
2.比较mid和right的值:
  a.如果mid.num < right.num 则为正序（第一种情况的序列和第二种情况的前一个序列），那么target如果在mid和right之间,则left=mid+1，否则right=mid;
  b.如果mid.num >= right.num，则为两个正序的序列（第二种情况），那么，target如果在mid和left之间，则right=mid，否则left=mid+1.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0)
            return -1;
        int left = 0;
        int right = nums.size() - 1;

        if (target < nums[left] && target > nums[right])
            return -1;

        int mid = 0;
        while (left < right) {
            mid = (left + right)/2;
            if (nums[mid] <= nums[right])
                if (target > nums[mid] && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid;
            else 
                if (target <= nums[mid] && target >= nums[left])
                    right = mid;
                else
                    left = mid + 1;
        }

        if (nums[left] == target)
            return left;
        return -1;

    }
};

int main(int argc, char** argv)
{
    Solution a;
    
    vector<int> nums;
    nums.push_back(3);
    nums.push_back(1);
    int res = a.search(nums, 3);
    cout<<res<<endl;

    return 0;
}
