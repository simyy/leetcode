/*
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Analysis:
同理3SUM，不同之处是记录最小差值的SUM，不断比较。
需要注意的是，由于差值取的abs绝对值（SUM-TARGET可正可负），必须判断left和right移动的方向。
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution
{
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int result = nums[0] + nums[1] + nums[2];
        int size = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < size; i++) {
            if (i > 0 && nums[i] == nums[i-1]) 
                continue;
            int left = i + 1;
            int right = size -1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right]; 
                if (sum == target)
                    return sum;

                if (abs(sum - target) < abs(result - target))
                    result = sum;

                if (sum > target) {
                    right--;
                    while (nums[right] == nums[right+1] && left < right) right--;
                }
                else if (sum < target) {
                    left ++;
                    while (nums[left] == nums[left-1] && left < right) left++;
                }
            }
        }
        return result;
    }
};

int main(int argc, char** argv)
{
    Solution a;

    int d[] = {0, 2, 1, -3};
    vector<int> x (d, d+4);

    int r = a.threeSumClosest(x, 1);
    cout<<r<<endl;

    return 0;
}
