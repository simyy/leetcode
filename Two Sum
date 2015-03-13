/*
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
/*

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        vector<int> result; 

        map<int, int> m;
        for (int i = 0; i != numbers.size(); ++i) {
            m.insert(pair<int, int>(numbers[i], i));
        }
        for (int i = 0; i != numbers.size(); ++i) {
            map<int, int>::iterator f = m.find(target - numbers[i]);
            if ((f != m.end()) && (i != f->second)) {
                if (i < f->second) {
                    result.push_back(i+1);
                    result.push_back(f->second+1);
                }
                else {
                    result.push_back(f->second+1);
                    result.push_back(i+1);
                }
                break;
            }
        }
        return result;
    }
};


int main(int argc, char** argv)
{

    vector<int> numbers;
    numbers.push_back(3);
    numbers.push_back(2);
    numbers.push_back(4);

    Solution a;
    vector<int> r = a.twoSum(numbers, 6);

    for (vector<int>::iterator i = r.begin(); i != r.end(); ++i) {
        cout<<*i<<endl;
    }

    return 0;
}
