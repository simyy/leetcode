/*
Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*/
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        int i = 0;
        while (i < len) {
           if (nums[i] == val) {
                nums.erase(nums.begin()+i);
                len--;
           } 
           else
               i++;
        }
    }
};
