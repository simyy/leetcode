/*
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Analysis:
此题主要考察二分法，情况分为：
1.mid>target，那么right=target目标在左侧
2.mid<target，那么left=target目标在右侧
3.left=target && right=target，那么找到左右端点，结束
4.left=target，找到左端点,right--
5.right=target，找到右端点,left++
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res;
        res.push_back(-1);
        res.push_back(-1);
        if (nums.size() == 0)
            return res;
        int left = 0;
        int right = nums.size() - 1;

        int mid = 0;
        while (left <= right) {
            if (nums[left] == target && nums[right] == target){
                res[0] = left;
                res[1] = right;
                return res;
            }
            mid = (left + right)/2;
            if (nums[mid] < target)
                left = mid + 1;
            else if (nums[mid] > target)
                right = mid - 1;
            else if (nums[left] == target) 
                right--;
            else if (nums[right] == target)
                left++;
            else {
                left++;
                right--;
            }
        }
        return res;

    }
};

int main(int argc, char** argv)
{
    Solution a;
    
    vector<int> nums;
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(3);
    vector<int> res  = a.searchRange(nums, 2);
    for(int i = 0; i < res.size(); ++i)
        cout<<res[i]<<" ";
    cout<<endl;

    return 0;
}
