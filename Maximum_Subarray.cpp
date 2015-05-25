/*
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Analysis:
1.use last to record the last sum, and use max to record the max sum;
2.compare last and max, then find the max.
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        int max = nums[0];
        int last = 0;
        for (int i = 0; i < nums.size(); ++i) {
            last += nums[i];
            if (max < last)
                max = last;
            if (last < 0)
                last = 0;
        }
        return max;
    }
};
